<template>
    <div>
        <l-map :zoom.sync="zoom" :center.sync="center" id="map" ref="myMap">
            <l-control-layers :position="'topright'" :collapsed="false" :sort-layers="false" />
            <l-tile-layer
                v-for="tileProvider in tileProviders.simple"
                :key="tileProvider.name"
                :name="tileProvider.name"
                :visible="tileProvider.visible"
                :url="tileProvider.url"
                :attribution="tileProvider.attribution"
                layer-type="base"
                :detectRetina="tileProvider.detectRetina"
                :options="{ minZoom: 1, maxZoom: 20, maxNativeZoom: 18 }"
                :subdomains="tileProvider.subdomains"
            />
            <l-wms-tile-layer
                v-for="wmsLayer in tileProviders.wms"
                :key="wmsLayer.name"
                :base-url="wmsLayer.url"
                :layers="wmsLayer.layers"
                :visible="wmsLayer.visible"
                :name="wmsLayer.name"
                :attribution="wmsLayer.attribution"
                :transparent="true"
                format="image/png"
                layer-type="base"
                :options="{ minZoom: 1, maxZoom: 20, maxNativeZoom: 18 }"
            />

            <l-control-scale :imperial="false" :position="'bottomleft'" />

            <l-layer-group ref="features">
                  <l-popup class="popup-wrap" :options="{offset:[1, -30]}">
                        <div class="image" :style="{ backgroundImage: 'url(images/gallery/' + caller.id + '.jpg)' }"></div>
                        <div class="content">
                            {{ [caller.region, caller.parish, caller.location].filter(Boolean).join(', ') }}<br />
                            {{ [caller.title, caller.type, caller.date].filter(Boolean).join(', ') }}<br />
                        </div>
                        <div class="manage">
                            <hr />
                            <div>
                                <div>
                                    <input type="checkbox" v-model="caller.draggable" :id="'cb' + caller.id" />
                                    <label :for="'cb' + caller.id">Labot</label>
                                </div>
                                <div>
                                    <select v-model="caller.status" @change="caller.datetime=dateNow()">
                                        <option value=1>Saglabājies</option>
                                        <option value=2>Tiek diskutēts</option>
                                        <option value=3>Pārvietots</option>
                                        <option value=0>Nojaukts</option>
                                    </select>
                                </div>
                                <div>id: {{ caller.id }}</div>
                            </div>
                        </div>
                    </l-popup>
            </l-layer-group>

             <l-layer-group
                layer-type="overlay"
                name="Bez apbed."
                :visible.sync="vislay[0]"
            ></l-layer-group>
            
            <l-layer-group
                layer-type="overlay"
                name="Ar apbed."
                :visible.sync="vislay[1]"
            ></l-layer-group>

            <v-marker-cluster 
                :options="{
                    chunkedLoading: true,
                    spiderfyOnMaxZoom: false,
                    showCoverageOnHover: false,
                    maxClusterRadius: '75',
                    disableClusteringAtZoom: '11'}"
            >
                <l-marker
                    v-for="marker in mdUpdate"
                    :key="marker.id"
                    :visible="marker.visible"
                    :draggable="marker.draggable"
                    :latLng.sync="marker.position"
                    :icon="myIcn[+marker.draggable][marker.status][marker.burial]"
                    @dragstart="closeMyPopup"
                    @dragend="marker.datetime=dateNow()"
                    @click="openMyPopup(marker)"
                >
                </l-marker>
            </v-marker-cluster>

        </l-map>
        <VList :md="mdUpdate" />
    </div>
</template>

<script>
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LMarker, LLayerGroup, LPopup, LControlScale, LControlLayers, LWMSTileLayer } from "vue2-leaflet";
import Vue2LeafletMarkerCluster from "vue2-leaflet-markercluster";

import { Icon } from "leaflet";
import VList from './VList.vue'

delete Icon.Default.prototype._getIconUrl;
var baseIcon = Icon.Default.extend({
    options: {
        shadowUrl: "images/leaflet/marker-shadow.png",
        iconSize: [25, 40],
        iconAnchor: [12, 41],
        popupAnchor: [0, -34],
        shadowSize: [41, 41],
    },
});

const greyIcon = new baseIcon({
    iconUrl: "images/leaflet/marker-grey.png",
    iconRetinaUrl: "images/leaflet/marker-grey.png",
});
const blueIcon = new baseIcon({
    iconUrl: "images/leaflet/marker-blue.png",
    iconRetinaUrl: "images/leaflet/marker-blue.png",
});
const blue2Icon = new baseIcon({
    iconUrl: "images/leaflet/marker-blue2.png",
    iconRetinaUrl: "images/leaflet/marker-blue2.png",
});
const redIcon = new baseIcon({
    iconUrl: "images/leaflet/marker-red.png",
    iconRetinaUrl: "images/leaflet/marker-red.png",
});

const greyIconEdit = new baseIcon({
    iconUrl: "images/leaflet/marker-grey-edit.png",
    iconRetinaUrl: "images/leaflet/marker-grey-edit.png",
});
const blueIconEdit = new baseIcon({
    iconUrl: "images/leaflet/marker-blue-edit.png",
    iconRetinaUrl: "images/leaflet/marker-blue-edit.png",
});
const blue2IconEdit = new baseIcon({
    iconUrl: "images/leaflet/marker-blue2-edit.png",
    iconRetinaUrl: "images/leaflet/marker-blue2-edit.png",
});
const redIconEdit = new baseIcon({
    iconUrl: "images/leaflet/marker-red-edit.png",
    iconRetinaUrl: "images/leaflet/marker-red-edit.png",
});

const icons = [
    [[greyIcon, greyIcon], [blueIcon, blue2Icon], [redIcon, redIcon], [blueIcon, blue2Icon]],
    [[greyIconEdit, greyIconEdit], [blueIconEdit, blue2IconEdit], [redIconEdit, redIconEdit], [blueIconEdit, blue2IconEdit]]
];

const tileProviders = {
    simple:[
        {
            name: "OSM",
            visible: true,
            attribution: '&copy; <a target="_blank" href="http://osm.org/copyright">OSM</a>',
            url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        },
        // {
        //     name: "Esri",
        //     visible: false,
        //     attribution: "Tiles &copy; Esri",
        //     url: "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
        // },
        {
            name: "J.Sēta",
            visible: false,
            attribution: '<a href="https://www.kartes.lv/en" target="_blank">Jāņa Sēta</a>',
            subdomains: ["wms", "wms1", "wms2", "wms3", "wms4"],
            url: "https://{s}.kartes.lv/LAUC/wgs/15/{z}/{x}/{y}.png"
        },
    ],
    wms:[
        {
            name: "Orto LKS",
            visible: false,
            attribution: '<a href="" target="_blank">LVM</a>',
            layers: 'public:Orto_LKS',
            url: "https://lvmgeoserver.lvm.lv/geoserver/ows?"
        },
        {
            name: "Topo10",
            visible: false,
            attribution: '<a href="" target="_blank">LVM</a>',
            layers: 'public:Topo10_contours',
            url: "https://lvmgeoserver.lvm.lv/geoserver/ows?"
        },
        {
            name: "PSRS",
            visible: false,
            attribution: '<a href="" target="_blank">GISnet</a>',
            layers: 'DT_KOPA',
            url: "https://www.gisnet.lv/cgi-bin/topo_all?"
        }, 
    ]
}

export default {
    name: "VMap",
    components: {
        LMap,
        LTileLayer,
        LMarker,
        LLayerGroup,
        LPopup,
        LControlScale,
        LControlLayers,
        "v-marker-cluster": Vue2LeafletMarkerCluster,
        "l-wms-tile-layer": LWMSTileLayer,
        VList,
    },
    props: { md: Array },
    data() {
        return {
            vislay: [true, true],
            caller: {id: null},
            myIcn: icons,
            center: [56.74, 24.12],
            zoom: 7,
            tileProviders: tileProviders,
        };
    },
    mounted() {
        if (localStorage.vislay) {
            this.vislay = JSON.parse(localStorage.vislay)
        }
    },
    watch: {
        vislay() {
            localStorage.vislay = JSON.stringify(this.vislay)
        },
    },
    computed: {
        mdUpdate() {
            return this.md.map(item => {
                item.visible= (item.burial === 0) ? this.vislay[0] : this.vislay[1]
                return item
            });
        }
    },
    methods: {
        dateNow(){
            return new Date().toJSON()
        },
        centerMyPopup(n){
            this.closeMyPopup()
            this.$nextTick(() => {
                this.$refs.myMap.mapObject.setView(n.position, (this.zoom >= 13) ? this.zoom : 13); 
                setTimeout(() => { this.openMyPopup(n) }, 700)
            });
        },
        closeMyPopup(){
            this.$refs.features.mapObject.closePopup()
        },
        openMyPopup(n){
            this.caller = n;
            this.$refs.features.mapObject.openPopup(n.position);
            // remove close href
            document.querySelector(".leaflet-popup-close-button").removeAttribute("href")
        },
        // alert2(v){
        // this.markers2.map((obj) => ({ ...obj, visible: true }))
        // console.log(v)
        // },
        // addMarker() {
        //     function rndNumber(min, max) {
        //         return Math.random() * (max - min) + min;
        //     }
        //     const pos = {
        //         lat: 57.11835 + rndNumber(-0.05, 0.05),
        //         lng: 23.66455 + rndNumber(-0.05, 0.05),
        //     };
        //     const newMarker = {
        //         id: this.markers.length + 1,
        //         position: pos,
        //         draggable: true,
        //         status: 2,
        //     };
        //     this.markers.push(newMarker);
        //     this.$refs.myMap.mapObject.setView(pos, 11);
        // },
        // removeMarker(index) {
        //     this.markers.splice(index, 1);
        // },
    },
};
</script>

<style>
@import "~leaflet.markercluster/dist/MarkerCluster.css";
@import "~leaflet.markercluster/dist/MarkerCluster.Default.css";

#app,
#app > div,
#map {
    height: 100%;
}

#map {
    width: 100%;
}

#map .leaflet-popup-content {
    width: 260px;
}

#map hr {
    border: 0;
    height: 1px;
    background-color: rgb(237, 237, 237);
    margin: 6px 0 14px;
}

#map .leaflet-popup-content {
    margin: 14px 14px 14px 14px;
}

/* .leaflet-marker-draggable{
    filter: hue-rotate(180deg);
} */

.leaflet-popup-close-button{
    cursor: pointer;
}

.popup-wrap{
    display: flex;
    flex-wrap: wrap;
}

.popup-wrap .image{
    width: 70px;
    height: 70px;
    background-size: cover;
    background-color: #f0eef1;
}

.popup-wrap .content{
    width: calc(100% - 80px);
    margin-left: 10px;
}

.popup-wrap .manage{
    width:100%;
    line-height: 1.5;
}

.popup-wrap .manage > div{
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.popup-wrap .manage label{
    cursor: pointer;
}

.popup-wrap .manage input{
    vertical-align: bottom;
}

.popup-wrap,
.popup-wrap .manage select{
    font-size: 12px;
}

@media (min-width: 600px) {
    #map {
        height: 50%;
    }

    #map .leaflet-popup-content {
        width: 320px;
    }
}

/* override clusters */
#map .marker-cluster-medium div {
    background-color: rgba(244, 183, 16, 0.9);
}

#map .marker-cluster-medium {
    background-color: rgba(246, 190, 58, 0.448);
}
</style>

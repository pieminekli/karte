<template>
    <div>
        <l-map :zoom.sync="zoom" :center.sync="center" id="map" ref="myMap">
            <l-control-layers :position="'topright'" :collapsed="false" :sort-layers="false" />
            <l-tile-layer
                v-for="tileProvider in tileProviders"
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
            <l-control-scale :imperial="false" :position="'bottomleft'" />
            <v-marker-cluster :options="clusterOptions">
                <l-marker
                    v-for="marker in markers"
                    :key="marker.id"
                    :draggable="marker.draggable"
                    :latLng.sync="marker.position"
                    :icon="myIcn[+marker.draggable][marker.status]"
                    ref="marker"
                    @dragend="marker.datetime=dateNow()"
                    @popupopen="popupFix"
                >
                    <l-popup class="popup-wrap">
                        <div class="image" :style="{ backgroundImage: 'url(images/gallery/' + marker.id + '.jpg)' }"></div>
                        <div class="content">
                            {{ [marker.region, marker.parish, marker.location].filter(Boolean).join(', ') }}<br />
                            {{ [marker.name, marker.type, marker.date1].filter(Boolean).join(', ') }}<br />
                        </div>
                        <div class="manage">
                            <hr />
                            <div>
                                <div>
                                <input v-model="marker.draggable" type="checkbox" :id="'cb' + marker.id" />
                                <label :for="'cb' + marker.id">Labot</label>
                                </div>
                                <div>
                                   Statuss:
                                    <select v-model="marker.status" @change="marker.datetime=dateNow()">
                                        <option value=1>Saglabājies</option>
                                        <option value=2>Tiek diskutēts</option>
                                        <option value=0>Nojaukts</option>
                                    </select>
                                </div>
                                <!-- <div>Slēgts: {{ marker.locked }}</div> -->
                                <div>id: {{ marker.id }}</div>
                            </div>
                        </div>
                    </l-popup>
                </l-marker>
            </v-marker-cluster>
        </l-map>
        <VList :md="markers" />
    </div>
</template>

<script>
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LMarker, LPopup, LControlScale, LControlLayers } from "vue2-leaflet";
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
const redIconEdit = new baseIcon({
    iconUrl: "images/leaflet/marker-red-edit.png",
    iconRetinaUrl: "images/leaflet/marker-red-edit.png",
});

const icons = [[greyIcon, blueIcon, redIcon], [greyIconEdit, blueIconEdit, redIconEdit]];

const clusterOptions = {
    chunkedLoading: true,
    spiderfyOnMaxZoom: false,
    showCoverageOnHover: false,
    maxClusterRadius: "70",
    disableClusteringAtZoom: "11",
};

const tileProviders = [
    {
        name: "OSM",
        visible: true,
        attribution: '&copy; <a target="_blank" href="http://osm.org/copyright">OSM</a>',
        url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        //  detectRetina: true,
        //  :tileSize="512"
        //  :options="{ zoomOffset:-1 }"
    },
    {
        name: "Esri",
        visible: false,
        attribution: "Tiles &copy; Esri",
        url: "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    },
    {
        name: "J.Sēta",
        visible: false,
        attribution: '<a href="https://www.kartes.lv/en" target="_blank">Jāņa Sēta</a>',
        subdomains: ["wms", "wms1", "wms2", "wms3", "wms4"],
        url: "https://{s}.kartes.lv/LAUC/wgs/15/{z}/{x}/{y}.png"
    }
];

export default {
    name: "VMap",
    components: {
        LMap,
        LTileLayer,
        LMarker,
        LPopup,
        LControlScale,
        LControlLayers,
        "v-marker-cluster": Vue2LeafletMarkerCluster,
        VList,
    },
    props: { md: Array },
    data() {
        return {
            myIcn: icons,
            isActive: false,
            clusterOptions: clusterOptions,
            center: [56.74, 24.12],
            zoom: 7,
            tileProviders: tileProviders,
            markers: this.md,
        };
    },
    methods: {
        // alert(item) {
            // alert('this is ' + JSON.stringify(item));
            // this.$refs.myMap.mapObject.setView(item.position);
            // var rect = item.getBoundingClientRect();
            // console.log(rect.top, rect.right, rect.bottom, rect.left);
            // console.log(this.$refs.marker[item.id]);
            // console.log(this.$refs.myMap.mapObject.project(item.position, this.zoom))
            // console.log(this.$refs.marker[item.id])
        // },
        dateNow(){
            return new Date().toJSON()
        },
        addMarker() {
            function rndNumber(min, max) {
                return Math.random() * (max - min) + min;
            }
            const pos = {
                lat: 57.11835 + rndNumber(-0.05, 0.05),
                lng: 23.66455 + rndNumber(-0.05, 0.05),
            };
            const newMarker = {
                id: this.markers.length + 1,
                position: pos,
                draggable: true,
                status: 2,
            };
            this.markers.push(newMarker);
            this.$refs.myMap.mapObject.setView(pos, 11);
        },
        removeMarker(index) {
            this.markers.splice(index, 1);
        },
        centerPopup(n) {
            let selMark = this.markers[n - 1];
            this.$nextTick(() => {
                this.$refs.myMap.mapObject.setView(selMark.position, 13);
                let xx = this.$refs.marker[n - 1].mapObject;
                setTimeout(function () {
                    xx.openPopup();
                }, 700);
            });
        },
        popupFix(){
            // remove close href
            document.querySelector(".leaflet-popup-close-button").removeAttribute("href")
        }
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
    max-width: 260px;
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
        max-width: 320px;
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

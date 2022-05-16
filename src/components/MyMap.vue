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
            />
            <l-control-scale :imperial="false" :position="'bottomleft'" />
            <v-marker-cluster :options="clusterOptions">
                <l-marker
                    v-for="marker in markers"
                    :key="marker.id"
                    :visible="marker.visible"
                    :draggable="marker.draggable"
                    :lat-lng.sync="marker.position"
                    :icon="myIc[marker.status]"
                    ref="marker"
                   
                >
                    <l-popup>
                        Nr: {{ marker.id }}<br />
                        {{ marker.region }}, {{ marker.parish }}, {{ marker.location }}<br />
                        {{ marker.name }}, {{ marker.date1 }}<br />
                        <hr />
                        <input v-model="marker.draggable" type="checkbox" :id="'cb' + marker.id" />
                        <label :for="'cb' + marker.id">Move marker</label>
                    </l-popup>
                </l-marker>
            </v-marker-cluster>
        </l-map>
        <!-- <BtnDownload :md="md" @updEvent="updateData"/> -->

        <div id="xlist2">
            <!-- <button name="button" @click="addMarker">Add a marker</button> -->
            <table>
                <tr>
                    <th>nr</th>
                    <th>region</th>
                    <th>location</th>
                    <th>name</th>
                    <th>date</th>
                    <th>description</th>
                    <th>lat</th>
                    <th>lng</th>
                    <th>move</th>
                    <!-- <th>Remove</th> -->
                </tr>
                <tr v-for="item in markers" :key="item.id" @click="posMark(item.id)">
                    <td>{{ item.id }}</td>
                    <td>{{ item.region }}</td>
                    <td>{{ item.parish }}, {{ item.location }}</td>
                    <td>{{ item.name }}</td>
                    <td>{{ item.date1 }}</td>
                    <td>{{ item.description }}</td>
                    <!-- <td>
            <input v-model="item.name" type="text" />
          </td>
          <td>
            <input v-model="item.description" type="text" />
          </td> -->

                    <td>{{ item.position.lat }}</td>
                    <td>{{ item.position.lng }}</td>

                    <td style="text-align: center">
                        <input v-model="item.draggable" type="checkbox" />
                    </td>

                    <!-- <td style="text-align: center">
            <input
              type="button"
              value="X"
              @click="removeMarker(index)"
            >
          </td> -->
                </tr>
            </table>
        </div>
    </div>
</template>

<script>
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LMarker, LPopup, LControlScale, LControlLayers } from "vue2-leaflet";

import Vue2LeafletMarkerCluster from "vue2-leaflet-markercluster";

// import BtnDownload from './GenCsv.vue'

import { Icon } from "leaflet";
delete Icon.Default.prototype._getIconUrl;

var baseIcon = Icon.Default.extend({
    options: {
        shadowUrl: "images/leaflet/marker-shadow.png",
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
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

const icons = [greyIcon, blueIcon, redIcon];

const clusterOptions = {
    chunkedLoading: true,
    spiderfyOnMaxZoom: false,
    showCoverageOnHover: false,
    maxClusterRadius: "60",
    disableClusteringAtZoom: "11",
};

const tileProviders = [
    {
        name: "OSM",
        visible: true,
        attribution: '&copy; <a target="_blank" href="http://osm.org/copyright">OSM</a>',
        url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        detectRetina: true,
        //  :tileSize="512"
        //  :options="{ zoomOffset:-1 }"
    },
    {
        name: "Esri",
        visible: false,
        url: "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
        attribution: "Tiles &copy; Esri",
    },
];

function randomNumber(min, max) {
    return Math.random() * (max - min) + min;
}

export default {
    name: "vue-map",
    components: {
        LMap,
        LTileLayer,
        LMarker,
        LPopup,
        LControlScale,
        LControlLayers,
        "v-marker-cluster": Vue2LeafletMarkerCluster,
        //  BtnDownload,
    },
    props: { md: Array },
    data() {
        return {
            myIc: icons,
            isActive: false,

            clusterOptions: clusterOptions,

            center: [56.74, 24.12],
            zoom: 7,
            tileProviders: tileProviders,

            markers: this.md,
        };
    },
    methods: {
    alert(item) {
    //   alert('this is ' + JSON.stringify(item));
    // this.$refs.myMap.mapObject.setView(item.position);
    },
        addMarker: function () {
            const pos = {
                lat: 57.11835 + randomNumber(-0.05, 0.05),
                lng: 23.66455 + randomNumber(-0.05, 0.05),
            };
            const newMarker = {
                id: this.markers.length + 1,
                position: pos,
                draggable: true,
                status: 2, //set icon
            };
            this.markers.push(newMarker);
            this.$refs.myMap.mapObject.setView(pos, 11);
        },
        removeMarker: function (index) {
            this.markers.splice(index, 1);
        },
        posMark(n) {
            let selMark = this.markers[n - 1];
            this.$nextTick(() => {
                this.$refs.myMap.mapObject.setView(selMark.position, 13);
                let xx = this.$refs.marker[n - 1].mapObject;
                setTimeout(function () {
                    xx.openPopup();
                }, 800);
            });
            // console.log( selMark )
        },
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

#xlist2 {
    display: none;
}

#map .leaflet-popup-content {
    max-width: 260px;
}

#map hr {
    border: 0;
    height: 1px;
    background-color: rgb(237, 237, 237);
}

@media (min-width: 600px) {
    #map {
        height: 50%;
    }

    #map .leaflet-popup-content {
        max-width: 320px;
    }

    #xlist2 {
        font-size: 12px;
        display: block;
        height: 50%;
        overflow: scroll;
        overflow-x: hidden;
    }

    #xlist2 button {
        position: fixed;
        bottom: 20px;
        right: 40px;
        color: white;
        background: #328bf2;
        padding: 8px;
        border: none;
        border-radius: 5px;
    }

    /* #xlist2 tr:nth-child(even){background-color: #f2f2f2;} */

    #xlist2 tr:hover {
        background-color: rgba(20, 116, 250, 0.1);
    }

    #xlist2 table {
        width: 100%;
        border-collapse: collapse;
    }
    #xlist2 th,
    td {
        border: 1px solid #ddd;
        padding: 8px;
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

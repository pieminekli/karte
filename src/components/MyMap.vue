<template>
  <div>
    <l-map
      :zoom.sync="zoom"
      :center.sync="center"
      :bounds=null
      :min-zoom="minZoom"
      :max-zoom="maxZoom"
      id="map"
      ref="myMap"
      :noBlockingAnimations="true"
    >
      <l-control-layers
        :position="layersPosition"
        :collapsed="false"
        :sort-layers="false"
      />
       <l-tile-layer
        v-for="tileProvider in tileProviders"
        :key="tileProvider.name"
        :name="tileProvider.name"
        :visible="tileProvider.visible"
        :url="tileProvider.url"
        :attribution="tileProvider.attribution"
        layer-type="base"
        :detectRetina="tileProvider.detectRetina"
      />

      <!-- <l-control :position="'topleft'">
        <div id="btn-edit" @click="toggleEdit" :class="{ active: isActive }"></div>
      </l-control> -->

      <l-control-scale :imperial="false" :position="'bottomleft'"/>

      <!-- <l-layer-group
        layer-type="overlay"
        name="Edit"
      > -->

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
        <l-popup >
            {{marker.id}}<br/>
            {{marker.region}}, {{marker.parish}}, {{marker.location}}<br/>
            {{marker.name}}<br/>
            {{marker.description}}<br/>
            Edit: <input v-model="marker.draggable" type="checkbox" >
        </l-popup>
        <!-- <l-icon
          :icon-anchor="staticAnchor"
          class-name="someExtraClass"> -->
            <!-- <svg
                width="24"
                height="40"
                viewBox="0 0 100 100"
                version="1.1"
                preserveAspectRatio="none"
                xmlns="http://www.w3.org/2000/svg"
                >
                <path d="M0 0 L50 100 L100 0 Z" fill="#7A8BE7"></path>
            </svg> -->
        <!-- </l-icon> -->
      </l-marker>
      </v-marker-cluster>

 
      <!-- </l-layer-group> -->

    </l-map>
    <!-- <BtnDownload :md="md" @updEvent="updateData"/> -->

    <div id="xlist2">
      <button
        name="button"
        @click="addMarker"
      >
        Add a marker
      </button>
      <table>
        <tr>
          <th>id</th>
          <th>Latitude</th>
          <th>Longitude</th>
          <th>name</th>
          <th>descr</th>
          <th>drag</th>
          <!-- <th>Remove</th> -->
        </tr>
        <tr
          v-for="(item) in markers"
          :key="item.id" @click="posMark(item.id)"
        >
          <td>{{item.id}}</td>
          <td>
            <input
              v-model.number="item.position.lat"
              type="number"
            >
          </td>
          <td>
            <input
              v-model.number="item.position.lng"
              type="number"
            >
          </td>
          <td>
            <input
              v-model="item.name"
              type="text"
            >
          </td>
          <td>
            <input
              v-model="item.description"
              type="text"
            >
          </td>
          <td style="text-align: center">
            <input
              v-model="item.draggable"
              type="checkbox"
            >
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
import 'leaflet/dist/leaflet.css';
import {
  LMap,
  LTileLayer,
  LMarker,
  LPopup,
  LControlScale,
  LControlLayers,
//   LControl,
//   LIcon,
} from 'vue2-leaflet';

import Vue2LeafletMarkerCluster from 'vue2-leaflet-markercluster'

// import BtnDownload from './GenCsv.vue'

import { Icon } from 'leaflet';

delete Icon.Default.prototype._getIconUrl;
// Icon.Default.mergeOptions({
//   iconRetinaUrl: require('../assets/leaflet/marker-blue.png'),
//   iconUrl: require('../assets/leaflet/marker-blue.png'),
//   shadowUrl: require('../assets/leaflet/marker-shadow.png'),
// });

var baseIcon = Icon.Default.extend({
    options: {
        shadowUrl: require('../assets/leaflet/marker-shadow.png'),
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowSize: [41, 41]
    }
});

const greyIcon = new baseIcon({iconUrl: require('../assets/leaflet/marker-grey.png')})
const blueIcon = new baseIcon({iconUrl: require('../assets/leaflet/marker-blue.png')})
const redIcon = new baseIcon({iconUrl: require('../assets/leaflet/marker-red.png')})

const icons = [
    greyIcon, blueIcon, redIcon
]


// let mymarks = [
//         {
//           id: 'm1',
//           position: { lat: 56.447313059250334, lng: 21.489257812500004 },
//           name: '<h1>tooltip for marker1</h1>',
//           draggable: true,
//           visible: true,
//           icon: icn,
//         },
//         {
//           id: 'm2',
//           position: { lat: 57.37393841871411, lng: 21.9122314453125 },
//           name: togdrag,
//           draggable: true,
//           visible: true,
//         },
//         {
//           id: 'm3',
//           position: { lat: 56.851975784517116, lng: 23.966674804687504 },
//           name: 'tooltip for marker3',
//           draggable: true,
//           visible: true,
//         },
//         {
//           id: 'm4',
//           position: { lat: 55.91842985630817, lng: 26.53198242187500 },
//           name: 'tooltip for marker4',
//           draggable: true,
//           visible: true,
//         },
//       ]

const clusterOptions = {
    chunkedLoading: true,
    spiderfyOnMaxZoom: false,
    showCoverageOnHover: false,
    maxClusterRadius: '60',
    disableClusteringAtZoom: '11'
}

const tileProviders = [
  {
    name: 'OSM',
    visible: true,
    attribution: '&copy; <a target="_blank" href="http://osm.org/copyright">OSM</a>',
    url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    detectRetina: true,
  },
  {
    name: 'Esri',
    visible: false,
    url: 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    attribution: 'Tiles &copy; Esri',
  },
];

function myFunction(d) {
    // const d_coord = d.coordinates.split(",");
    let obj = {}
    // const pos = {lat: parseFloat(d_coord[0]), lng: parseFloat(d_coord[1])}
    obj.id = d.id
    obj.region = d.region
    obj.parish = d.parish
    obj.location = d.location
    obj.name = d.name
    obj.description = d.description
    obj.position = {lat: d.lat, lng: d.lng}
    obj.draggable = false
    obj.icon = icons[d.status]
    // d.map(obj=> ({...obj, Active: 'false'})) // add new property to array
    return obj;
}


export default {
  name: 'MyExample',
  components: {
    LMap,
    LTileLayer,
    LMarker,
    // LPolyline,
    // LLayerGroup,
    // LTooltip,
    LPopup,
    // LControlZoom,
    // LControlAttribution,
    LControlScale,
    LControlLayers,
    // LIcon,
    // LControl,
    'v-marker-cluster': Vue2LeafletMarkerCluster,
    //  BtnDownload,
  },
  props: { md: Array },
  data() {
    return {
        myIc: icons,
      isActive: false,
      clusterOptions: clusterOptions,
      center: [56.74, 24.12],
    //   opacity: 0.6,
      zoom: 7,
      minZoom: 1,
      maxZoom: 20,
      layersPosition: 'topright',
      tileProviders: tileProviders,
    //   markers: this.md.map(myFunction),
    //   markers: mymarks,
    markers:this.md,

    };
  },
  watch: { 
        md: function(newVal, oldVal) { // watch it
          console.log('Prop changed: ', newVal, ' | was: ', oldVal)
        }
  },
  created() {
    //  console.log(this.md)
    //  const newArr = this.md.map(myFunction)
    //  console.log(newArr)
  },

  methods: {
    alert(item) {
        alert('this is ' + JSON.stringify(item));
    },
    addMarker: function() {
        const newMarker = {
            position: { lat: 57.11835002634525, lng: 23.664550781250004 },
            draggable: true,
            visible: true,
        };
        this.markers.push(newMarker);
    },
    removeMarker: function(index) {
        this.markers.splice(index, 1);
    },
    toggleEdit(){
        // alert("Click!");
        this.isActive = !this.isActive;
        // this.$emit('someEvent')
        // this.markers = this.markers.map(obj=> ({...obj, draggable: false}))
        // console.log(this.markers)
        // this.$refs.marker[92].mapObject.options.draggable=true
        // this.$refs.marker[92].mapObject.dragging.enable()
        // console.log(this.$refs.marker[92].mapObject)
    },
    posMark(n){
        let selMark = this.markers[n-1]
        this.$nextTick(() => {
            this.$refs.myMap.mapObject.setView(selMark.position, 13);
            let xx = this.$refs.marker[n-1].mapObject
            setTimeout(function(){
                xx.openPopup()
            }, 800);
        });
        // console.log( selMark )

    }

  },
};
</script>

<style >
@import "~leaflet.markercluster/dist/MarkerCluster.css";
@import "~leaflet.markercluster/dist/MarkerCluster.Default.css";

 #map { 
    height: 100vh; 
    width: 100%;
 }

#xlist2 {
    display: none;
}

#btn-edit{
    position: fixed;
    top: 80px;
    left: 12px;
    z-index: 100000;
    padding: 0;
    background: white;
    text-align: center;
    line-height: 30px;
    height: 30px;
    width: 30px;
    cursor: pointer;
    border-radius: 2px;
}
#btn-edit.active {
    background: rgb(249, 86, 119);
    color: white;
}
#btn-edit:before {
    content: '';
    width: 13px;
    height: 13px;
    position: absolute;
    left: 9px;
    top: 8px;
    display: block;
    /* background: url('/assets/leaflet/edit.svg') no-repeat; */
    background-color: black;
    -webkit-mask: url('@/assets/leaflet/edit.svg') no-repeat 50% 50%;
    mask: url('@/assets/leaflet/edit.svg') no-repeat 50% 50%;
    -webkit-mask-size: cover;
    mask-size: cover;
}
#btn-edit.active:before{
    background-color: white;
}

@media (min-width: 600px) {
    #map { 
        height: 50vh;
    }
    #xlist2 {
        display: block;
        height: 50vh;
        overflow: scroll;
        overflow-x: hidden;
    }
}

/* override clusters */
#map .marker-cluster-medium div{
    background-color: rgba(244, 183, 16, 0.9);
}

#map .marker-cluster-medium {
    background-color: rgba(246, 190, 58, 0.448);
}
</style>
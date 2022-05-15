<template>
<div style="height: 500px; width: 100%">
    <div style="height: 200px; overflow: auto;">
      <p>First marker is placed at {{ withPopup.lat }}, {{ withPopup.lng }}</p>
      <p>Center is at {{ currentCenter }} and the zoom is: {{ currentZoom }}</p>
      <button @click="showLongText">
        Toggle long popup
      </button>
      <button @click="showMap = !showMap">
        Toggle map
      </button>
    </div>
    <l-map
      v-if="showMap"
      :zoom="zoom"
      :center="center"
      :options="mapOptions"
      style="height: 80%"
      @update:center="centerUpdate"
      @update:zoom="zoomUpdate"
    >
      <l-tile-layer
        :url="url"
        :attribution="attribution"
        :detectRetina="retina"
      />
      <l-marker :lat-lng="withPopup" :draggable="true">
        <l-popup>
          <div @click="innerClick">
            I am a popup
            <p v-show="showParagraph">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque
              sed pretium nisl, ut sagittis sapien. Sed vel sollicitudin nisi.
              Donec finibus semper metus id malesuada.
            </p>
          </div>
        </l-popup>
      </l-marker>
      <l-marker :lat-lng="withTooltip">
        <l-tooltip :options="{ permanent: true, interactive: true }">
          <div @click="innerClick">
            I am a tooltip
            <p v-show="showParagraph">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque
              sed pretium nisl, ut sagittis sapien. Sed vel sollicitudin nisi.
              Donec finibus semper metus id malesuada.
            </p>
          </div>
        </l-tooltip>
      </l-marker>

      <l-marker
        v-for="marker in md"
        :key="marker.id"
        :draggable="true"
        :lat-lng="mysplit(marker.coordinates)"
        @click="alert(marker)"
      >
        <l-popup :content="marker.tooltip" />
      </l-marker>

    </l-map>
              
              
              <ul id="example-1">
            <li v-for="item in md" :key="item.id">
              {{ item.id }}, {{ item.name }}, {{ item.coordinates }}
            </li>
        </ul>
  </div>
</template>

<script>
import { latLng } from "leaflet";
import { LMap, LTileLayer, LMarker, LPopup, LTooltip } from "vue2-leaflet";

import MyData from '../assets/data.json';

import { Icon } from 'leaflet';
delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

export default {
  name: "MyMap",
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup,
    LTooltip
  },
  data() {
    return {
      md: MyData.data,

      zoom: 7,
      center: latLng(56.949650, 24.105186),
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      retina: true,

      cll:[],
      withPopup: latLng(56.949650, 24.105186),
      withTooltip: latLng(47.41422, -1.250482),
      currentZoom: 8,
      currentCenter: latLng(47.41322, -1.219482),
      showParagraph: false,
      mapOptions: {
        // zoomSnap: 0.5
      },
      showMap: true
    };
  },
  methods: {
    mysplit(v){
      var x = v.split(",")
      return{lat:x[0], lng:x[1]}
    },
    mytest(){
        this.cll = this.getLatLng();
    },
    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
    },
    showLongText() {
      this.showParagraph = !this.showParagraph;
    },
    innerClick() {
      alert("Click!");
    }
  }
};
</script>
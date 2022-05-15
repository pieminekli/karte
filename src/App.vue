<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <MyMap :md="md" @someEvent="toggleMethod()"/>
    <!-- <Xlist :md="md"/> -->
    <!-- <BtnDownload :md="md"/> -->
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import MyMap from './components/MyMap.vue'
// import MyTest from './components/MyTest.vue'
import Xlist from './components/MyList.vue'
import BtnDownload from './components/GenCsv.vue'

import 'leaflet/dist/leaflet.css';

import { Icon } from 'leaflet';

delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
  iconRetinaUrl: require('./assets/leaflet/marker-blue.svg'),
  iconUrl: require('./assets/leaflet/marker-blue.svg'),
  shadowUrl: require('./assets/leaflet/marker-shadow.png'),
});

import MyData from './assets/data.json';

export default {
  name: 'App',
  components: {
    // HelloWorld,
    // MyTest,
    MyMap,
    // Xlist,
    // BtnDownload,
},
data() {
  return {
    md: MyData,
  };
},
methods: {
  toggleMethod(){
    // this.md.map(obj=> ({...obj, draggable: 'false'}))
    // console.log(this.md)
  }
}
}
</script>

<style>
body{
  margin: 0;
  padding: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;

}

</style>

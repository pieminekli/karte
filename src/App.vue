<template>
  <div id="app">
    <MyMap :md="md" />
    <!-- <Xlist :md="md"/> -->
    <BtnDownload :md="md" @updEvent="updateData"/>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import MyMap from './components/MyMap.vue'
// import MyTest from './components/MyTest.vue'
// import Xlist from './components/MyList.vue'
import BtnDownload from './components/GenCsv.vue'


import MyData from './assets/data.json';
var MyData2=MyData.map(obj=> ({...obj, draggable: false})) // add new property to array

export default {
  name: 'App',
  components: {
    // HelloWorld,
    // MyTest,
    MyMap,
    // Xlist,
    BtnDownload,
},
data() {
  return {
    md: MyData2,
  };
},
methods: {
  updateData(n){
    // console.log(n[92])
    this.md=n
  },

}
}
</script>

<style>
html, body{
  margin: 0;
  padding: 0;
  height: 100%;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;

}

</style>

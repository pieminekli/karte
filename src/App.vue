<template>
    <div id="app">
        <VMap :md="md" />
        <VCsv :md="md" @updEvent="updateData" />
        <!-- <VList :md="md"/> -->
    </div>
</template>

<script>
import VMap from "./components/VMap.vue";
import VCsv from "./components/VCsv.vue";
import data from "./assets/data.json";
// import VList from './components/VList.vue'

// add drag property to array
var data2 = data.map((obj) => ({ ...obj, draggable: false }));

export default {
    name: "App",
    components: {
        VMap,
        VCsv,
        // VList,
    },
    data() {
        return {
            md: data2,
        };
    },
    methods: {
        updateData(n) {
            // console.log(n[92])
            // this.md = n;
        },
    },
};
</script>

<style>
html,
body {
    margin: 0;
    padding: 0;
    height: 100%;
    font-family: Arial, Helvetica, sans-serif;
}
</style>

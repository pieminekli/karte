<template>
    <div id="app">
        <VMap :md="md" />
        <VCsv :md="md" @updEvent="updateData" />
        <!-- <VList :md="md"/> -->

        <!-- <button id="show-modal" @click="showModal = true">Show Modal</button> -->
        <VModal v-if="showModal" @close="showModal = false">
            <h3 slot="header">Informācija</h3>

            <template #body>
                <p>Karte ir izstrādes stadijā! Lielākajai daļai marķieru atrašanās vieta ir aptuvena. </p>
                <p>Precizē marķieru atrašanās vietu zināmajiem pieminekļiem. </p>
                <p>Lejuplādē laboto *.csv failu un sūti uz pieminekli@protonmail.com </p>
                <p>Vai arī veic labojumus <a href="https://github.com/pieminekli/karte">github.com</a> </p>
            </template>
        </VModal>
    </div>
</template>

<script>
import VMap from "./components/VMap.vue";
import VCsv from "./components/VCsv.vue";
import VModal from "./components/VModal.vue";
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
        VModal,
    },
    data() {
        return {
            md: data2,
            showModal: true
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

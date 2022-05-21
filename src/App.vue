<template>
    <div id="app">
        <VMap :md="md" />
        <VCsv :md="md" @updEvent="updateData" />
        <VModal v-if="showModal" @close="showModal = false">
            <h3 slot="header">Informācija</h3>
            <template #body>
                <p>Karte ir izstrādes stadijā!</p> 
                <p>Daļai marķieru koordinātas ir aptuvenas. Precizē sev zināmajiem pieminekļiem atrašanās vietu, ieslēdzot labošanas režīmu un pārvietojot marķierus.</p>
                <p>Lejuplādē *.csv failu ar izmaiņām un sūti uz <a href="mailto:pieminekli@protonmail.com?subject=Kartes labojumi">pieminekli@protonmail.com</a>, pievieno trūkstošos attēlus, norādot pieminekļa id.</p>
                <p>Vai arī veic labojumus <a href="https://github.com/pieminekli/karte" target="_blank">github</a> patstāvīgi.</p>
            </template>
        </VModal>
    </div>
</template>

<script>
import VMap from "./components/VMap.vue";
import VCsv from "./components/VCsv.vue";
import VModal from "./components/VModal.vue";
import data1 from "./assets/data.json";
import data2 from "./assets/data2.json";

// add drag property to array
var data1_drag = data1.map((obj) => ({ ...obj, draggable: false, visible: true, burial:0 }));
var data2_drag = data2.map((obj) => ({ ...obj, draggable: false, visible: true, burial:1 }));

const merged = data1_drag.concat(data2_drag);

export default {
    name: "App",
    components: {
        VMap,
        VCsv,
        VModal,
    },
    data() {
        return {
            md: merged,
            // md2: data2_drag,
            showModal: true
        };
    },
    methods: {
        updateData(n) {
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

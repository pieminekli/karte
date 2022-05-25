<template>
    <div id="app">
        <VMap :md="md" />
        <VCsv :md="md" @updEvent="updateData" />
        <VModal v-if="showModal" @close="showModal = false">
            <h3 slot="header">Informācija</h3>
            <template #body>
                <p>Karte ir izstrādes stadijā!</p> 
                <p>Daļai marķieru koordinātas ir aptuvenas. Precizē sev zināmajiem pieminekļiem atrašanās vietu, ieslēdzot labošanas režīmu un pārvietojot marķierus.</p>
                <p>Lejuplādē *.csv failu ar labotajām marķieru koordinātēm un sūti uz <a href="mailto:pieminekli@protonmail.com?subject=Kartes labojumi">pieminekli@protonmail.com</a>, pievieno trūkstošos attēlus, norādot pieminekļa id.</p>
                <p>Vai arī veic labojumus <a href="https://github.com/pieminekli/karte" target="_blank">github</a> patstāvīgi.</p>
            </template>
        </VModal>
    </div>
</template>

<script>
import VMap from "./components/VMap.vue";
import VCsv from "./components/VCsv.vue";
import VModal from "./components/VModal.vue";
import data from "./assets/data.json";

// add drag property to array
for (const n of data){
    n.draggable = false
    n.visible = true
}
// console.log(data1)

export default {
    name: "App",
    components: {
        VMap,
        VCsv,
        VModal,
    },
    data() {
        return {
            md: data,
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

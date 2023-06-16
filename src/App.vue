<template>
    <div id="app">
        <VMap :md="md" ref="vmap"/>
        <VCsv :md="md" @updEvent="updateData" :modified="modified"/>
        <!-- <VModal v-if="showModal" @close="showModal = false">
            <h3 slot="header">Informācija</h3>
            <template #body>
                <p>Karte ir izstrādes stadijā!<br>Daļai marķieru koordinātas ir aptuvenas.</p> 
                <p>Kā precizēt pieminekļu atrašanās vietu:</p>
                <ol>
                    <li>Klikšķini uz marķiera, kuru vēlies precizēt.</li>
                    <li>Popup logā ieslēdz labošanas režīmu un pārvieto marķieri.</li>
                    <li>Lejuplādē *.csv failu ar veiktajām izmaiņām un sūti uz <a href="mailto:pieminekli@protonmail.com?subject=Kartes labojumi">pieminekli@protonmail.com</a>, pievieno trūkstošos attēlus, norādot pieminekļa id.</li>
                </ol>
                <p>Vai arī veic labojumus <a href="https://github.com/pieminekli/karte" target="_blank">github</a> patstāvīgi.</p>

                <div>Atjaunots: 13. jun. 2022</div>
            </template>
        </VModal> -->
    </div>
</template>

<script>
import VMap from "./components/VMap.vue";
import VCsv from "./components/VCsv.vue";
import VModal from "./components/VModal.vue";
import data from "./assets/data.json";

// add temp properties to array
for (let n of data){
    n.draggable = false
    n.visible = true
    n.edited = false
    n.previewUrl = ''
}

const results = data.filter(obj => {
  return obj.burial === 1;
});

// console.log(results)

export default {
    name: "App",
    components: {
        VMap,
        VCsv,
        // VModal,
    },
    data() {
        return {
            md: data,
            modified: false,
            showModal: true,
        };
    },
    methods: {
        updateData(n) {
            // this.md = n;
        },
    },
    mounted() {
        // console.log(this.md)
    },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Roboto');

html, body {
    margin: 0;
    padding: 0;
    height: 100%;
    font-family: 'Roboto', Arial, Helvetica, sans-serif;
}
</style>

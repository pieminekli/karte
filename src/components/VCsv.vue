<template>
    <!-- <a v-if="modified" :class="{modified: modified}" @click="sendData">Saglabāt..</a> -->
    <a v-if="modified" :class="{modified: modified}" :href="fileurl" :download="filename" @click="makeCsv">Lejuplādēt CSV</a>
    <a v-else :class="{modified: modified}" :href="fileurl" :download="filename" @click="makeCsv">Lejupādēt CSV</a>
</template>

<script>
export default {
    name: "VCsv",
    components: {},
    props: { md: Array, modified: Boolean },
    data() {
        return {
            fileurl: "#",
            filename: null,

            rMessage: null,
        };
    },

    methods: {
        // generate csv and download
        makeCsv() {
            let markers = this.md;
            // this.$emit("updEvent", markers);

            function checkField(d) {
                if (typeof d === "string") {
                    //replace quotes with double quotes
                    d = d.replace(/"/g, '""');
                    //if field has comma or quotes, wrap it with quotes
                    if (d.includes(",") || d.includes('"')) {
                        d = '"' + d + '"';
                    }
                }
                return d;
            }

            // function makeid() {
            //     var text = "";
            //     var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
            //     for (var i = 0; i < 6; i++)
            //         text += possible.charAt(Math.floor(Math.random() * possible.length));
            //     return text;
            // }

            let csvRows = "";
            for (const m of markers) {
                let row = [
                    m.id,
                    checkField(m.region),
                    checkField(m.parish),
                    checkField(m.location),
                    checkField(m.title),
                    checkField(m.date),
                    checkField(m.description),
                    checkField(m.type),
                    checkField(m.m_date),
                    checkField(m.m_author),
                    checkField(m.period),
                    checkField(m.army),
                    m.position.lat,
                    m.position.lng,
                    m.status,
                    m.burial,
                    m.locked,
                    checkField(m.url),
                    m.datetime
                ].join()
                csvRows += row + "\r\n";
            }
            // console.log(csvRows)

            var csvFile = new Blob([csvRows], {
                type: "text/csv;charset=utf-8;",
            });

            window.URL = window.URL || window.webkitURL;
            this.filename = "pieminekli.csv";
            this.fileurl = window.URL.createObjectURL(csvFile);
        },

        sendData(){

            // const uplArr = []

            // for (var n of this.$parent.$refs.vmap.$refs.vlist.$refs.vpreview){
            //     if(n.$refs.ifile.files.length > 0){
            //         uplArr.push(n.$refs.ifile.files[0])
            //         n.resetVal()
            //     }
            // }


            // var formData = new FormData();
            
            // const cleaned_arr = this.md.map(({draggable, visible, edited, previewUrl, ...remainingAttrs}) => remainingAttrs)
            // const jblob = new Blob([JSON.stringify(cleaned_arr)], {
            //     type: 'application/json'
            // });

            // formData.append("_special", "special");
            // formData.append("json_file", jblob, "file.json");

            // for (const n of uplArr) {
            //     formData.append('image_file[]', n, 'xxx--' + n.name);
            // }

            // // console.log(formData.getAll('image_file[]'))

            // this.rMessage = 'saving...'
 
            // setTimeout(() => {
            //     this.$parent.modified = false
            // }, 300)

        },

    },
};
</script>

<style scoped>
a {
    cursor: pointer;
    position: absolute;
    top: 0;
    right: 0;
    left: 0;
    z-index: 1001;
    margin: 12px 56px 0;
    background: rgba(255, 255, 255, 1);
    color: black;
    font-size: 12px;
    text-align: center;
    display: block;
    padding: 5px 10px;
    width: 100px;
    text-decoration: none;
    border-radius: 4px;
    box-shadow: 0px 0px 0px 2px rgba(0, 0, 0, 0.2);
}
a.modified {
    color: white;
    background: rgb(246, 68, 28);
}

@media (min-width: 600px) {
    a{
        left: 0;
        margin: 12px auto 0;
    }
}
</style>

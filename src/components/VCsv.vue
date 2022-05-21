<template>
    <a :href="fileurl" :download="filename" @click="makeCsv">Lejupādēt</a>
</template>

<script>
export default {
    name: "VCsv",
    components: {},
    props: { md: Array },
    data() {
        return {
            fileurl: "#",
            filename: null,
        };
    },
    methods: {
        // generate csv and download
        makeCsv() {
            let markers = this.md;
            // this.$emit("updEvent", markers);
            // console.log(this.md[92].position)

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
                    checkField(m.name),
                    checkField(m.date1),
                    checkField(m.description),
                    checkField(m.type),
                    checkField(m.date2),
                    m.position.lat,
                    m.position.lng,
                    m.status,
                    checkField(m.url),
                    m.locked,
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
    },
};
</script>

<style scoped>
a {
    position: absolute;
    top: 0;
    right: 140px;
    z-index: 1001;
    margin: 12px;
    background: rgba(255, 255, 255, 1);
    color: black;
    font-size: 12px;
    text-align: center;
    display: block;
    padding: 5px;
    width: 64px;
    text-decoration: none;
    border-radius: 4px;
    box-shadow: 0px 0px 0px 2px rgba(0, 0, 0, 0.2);
}
</style>

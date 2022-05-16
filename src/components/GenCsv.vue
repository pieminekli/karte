<template>
    <a :href="fileurl" :download="filename" @click="genCsv">Download</a>
</template>


<script>

export default {
  name: 'MyExample',
  components: {
  },
  props: {md: Array},
  data() {
    return {
        fileurl: '#',
        filename: null
    };
  },
  methods: {

    // generate csv and download
    genCsv: function () {
        var jdata = this.md
        this.$emit('updEvent', jdata)
        // console.log(this.md[92].position)

        function wrapq(d){
            if (d===String){
                // d = d.replaceAll('"', '""')
                d = d.replace(/"/g, '""')
                // .replace(/:insertx:/g, 'hello!');
                if (d.includes(",") || d.includes('"')){
                    d = '"'+d+'"'
                }
            }
            return d
        }

        // function makeid() {
        //     var text = "";
        //     var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        //     for (var i = 0; i < 6; i++)
        //         text += possible.charAt(Math.floor(Math.random() * possible.length));
        //     return text;
        // }

        let csv=''
        for (let d in jdata){
            let stri = ''
            stri += jdata[d].id+','
            stri += wrapq(jdata[d].region)+','
            stri += wrapq(jdata[d].parish)+','
            stri += wrapq(jdata[d].location)+','
            stri += wrapq(jdata[d].name)+','
            stri += wrapq(jdata[d].date1)+','
            stri += wrapq(jdata[d].description)+','
            stri += wrapq(jdata[d].type)+','
            stri += wrapq(jdata[d].date2)+','
            stri += wrapq(jdata[d].position.lat)+','
            stri += wrapq(jdata[d].position.lng)+','
            stri += jdata[d].status+','
            stri += wrapq(jdata[d].url)+','
            stri += jdata[d].locked+','
            stri += jdata[d].datetime+'\r\n'
            csv+=stri
            // console.log(stri)
            // console.log(wrapq(jdata[d].position.lat))
        }
        // console.log(csv)
  
    var fileContent = csv;
    var myFile = new Blob([fileContent], {type: 'text/csv;charset=utf-8;'});

    window.URL = window.URL || window.webkitURL;

    this.filename = 'pieminekli.csv'
    this.fileurl=window.URL.createObjectURL(myFile)
}


  },
};
</script>

<style scoped>
    a{
        position: fixed;
        top: 68px;
        right: 0;
        z-index: 100001;
        margin: 10px;

        background: rgba(255,255,255,1);
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

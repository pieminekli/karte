<template>
    <a href="#" id="btn-download" @click="genCsv()">Download CSV</a>
</template>


<script>

export default {
  name: 'MyExample',
  components: {
  },
  props: {md: Array},
  data() {
    return {
    //   md: MyData.data,
    };
  },
  methods: {

    // generate csv and download
    genCsv: function (jdata) {
        console.log(this.md)
    // function wrapq(d){
    //     d = d.replaceAll('"', '""')
    //     if (d.includes(",") || d.includes('"')){
    //         d = '"'+d+'"'
    //     }
    //     return d
    // }

    // let csv=''
    // for (let d in jdata){
    //     let stri = ''
    //     stri += jdata[d].id+','
    //     stri += wrapq(jdata[d].region)+','
    //     stri += wrapq(jdata[d].parish)+','
    //     stri += wrapq(jdata[d].location)+','
    //     stri += wrapq(jdata[d].name)+','
    //     stri += wrapq(jdata[d].date1)+','
    //     stri += wrapq(jdata[d].description)+','
    //     stri += wrapq(jdata[d].type)+','
    //     stri += wrapq(jdata[d].date2)+','
    //     stri += wrapq(jdata[d].coordinates)+','
    //     stri += jdata[d].status+','
    //     stri += wrapq(jdata[d].url)+','
    //     stri += jdata[d].locked+','
    //     stri += jdata[d].datetime+'\r\n'
    //     csv+=stri
    //     // console.log(stri)
    // }
    // // console.log(cs)
  

    // var fileName = "file.csv";
    // var fileContent = csv;
    // var myFile = new Blob([fileContent], {type: 'text/csv;charset=utf-8;'});

    // window.URL = window.URL || window.webkitURL;
    // var dlBtn = document.getElementById("btn-download");

    // dlBtn.setAttribute("href", window.URL.createObjectURL(myFile));
    // dlBtn.setAttribute("download", fileName);
}


  },
};
</script>

<style>
#btn-download{
    position: fixed;
    top: 0;
    right: 0;
    z-index: 100001;
    margin: 10px;

    background: rgba(70,142,189,0.8);
    color: white;
    font-size: 14px;
    text-align: center;
    display: block;
    padding: 10px;
    width: 110px;
    text-decoration: none;
    border-radius: 6px;
}
</style>
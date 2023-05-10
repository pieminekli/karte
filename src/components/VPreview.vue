<template>
    <label>
        <!-- <input class="file-hidden" ref="ifile" type="file" accept="image/*" @change="editItem" /> -->
        <div class="image">
            <img :src="genPreview" />
        </div>
    </label>
</template>

<script>
    export default {
        name: "VPreview",
        props: { itm: Object },
        data() {
            return {
                item: this.itm
            };
        },
        computed: {
            genPreview(){
                return this.item.edited? this.item.previewUrl : 'images/gallery/' + this.item.url
            }
        },
        methods: {
            editItem(){
                // this.$parent.$parent.dataChanged()
                // const file = this.$refs.ifile.files[0];

                // if (file) {
                //     this.item.previewUrl = URL.createObjectURL(file);
                //     this.item.edited = true
                // } else {
                //     this.item.edited = false
                // }
            },
            resetVal(){
                // this.item.edited = false
                // this.$refs.ifile.value = null
            },

        },
    };

</script>

<style scoped>
.file-hidden {
    width: 0.1px;
	height: 0.1px;
	opacity: 0;
	overflow: hidden;
	position: absolute;
	z-index: -1;
}

label {
    display: inline-block;
    cursor: pointer;
}

label .image {
    width: 60px;
    height: 60px;
}

label .image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
</style>
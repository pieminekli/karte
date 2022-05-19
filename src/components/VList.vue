<template>
    <div id="xlist">
            <!-- <button name="button" @click="addMarker">Add a marker</button> -->
            <table>
                <tr>
                    <th>id</th>
                    <th>region</th>
                    <th>location</th>
                    <th>name</th>
                    <th>description</th>
                    <th>date</th>
                    <th>type</th>
                    <th>lat</th>
                    <th>lng</th>
                    <th>move</th>
                    <!-- <th>Remove</th> -->
                </tr>
                <tr v-for="item in md" :key="item.id" @click="rowClick(item.id)">
                    <td>{{ item.id }}</td>
                    <td>{{ item.region }}</td>
                    <td>{{ [item.parish, item.location].filter(Boolean).join(', ') }}</td>
                    <td>{{ item.name }}</td>
                    <td>{{ item.description }}</td>
                    <td>{{ item.date1 }}</td>
                    <td style="width: 180px">{{ item.type }}</td>
                    <!-- <td>
                        <input v-model="item.name" type="text" />
                    </td>
                    <td>
                        <input v-model="item.description" type="text" />
                    </td> -->
                    <td>{{ item.position.lat }}</td>
                    <td>{{ item.position.lng }}</td>
                    <td style="text-align: center">
                        <input v-model="item.draggable" type="checkbox" />
                    </td>
                    <!-- <td style="text-align: center">
                        <input
                        type="button"
                        value="X"
                        @click="removeMarker(index)"
                        >
                    </td> -->
                </tr>
            </table>
        </div>
</template>

<script>
export default {
    name: "VList",
    components: {},
    props: { md: Array },
    data() {
        return {
            // markers: this.md,
        };
    },
    methods: {
        rowClick(n){
            this.$parent.centerPopup(n);
        }
    },
};
</script>

<style scoped>

#xlist {
    display: none;
}

@media (min-width: 600px) {
    #xlist {
        font-size: 12px;
        display: block;
        height: 50%;
        overflow: scroll;
        overflow-x: hidden;
    }

    #xlist button {
        position: fixed;
        bottom: 20px;
        right: 40px;
        color: white;
        background: #328bf2;
        padding: 8px;
        border: none;
        border-radius: 5px;
    }

    /* #xlist2 tr:nth-child(even){background-color: #f2f2f2;} */

    #xlist tr:hover {
        background-color: rgba(20, 116, 250, 0.1);
    }

    #xlist table {
        width: 100%;
        border-collapse: collapse;
    }
    #xlist th,
    td {
        border: 1px solid #ddd;
        padding: 8px;
    }
}
</style>

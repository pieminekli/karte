<template>
    <div id="xlist">
            <!-- <button name="button" @click="addMarker">Add a marker</button> -->
            <table>
                <tr>
                    <th>id</th>
                    <th>Reģions</th>
                    <th>Atrašanās vieta</th>
                    <th>Nosaukums</th>
                    <th>Apraksts</th>
                    <th>Datējums</th>
                    <th>Veids</th>
                    <th>Koordinātes</th>
                    <th>Labot</th>
                    <!-- <th>Remove</th> -->
                </tr>
                <tr v-for="item in md" v-show="item.visible" :key="item.id" @click="$parent.centerMyPopup(item)">
                    <td>{{ item.id }}</td>
                    <td>{{ item.region }}</td>
                    <td>{{ [item.parish, item.location].filter(Boolean).join(', ') }}</td>
                    <td>{{ item.title }}</td>
                    <td>{{ item.description }}</td>
                    <td>{{ item.date }}</td>
                    <td>{{ item.type }}</td>
                    <td style="width: 180px">{{ item.position.lat }},<br/>{{ item.position.lng }}</td>
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

            <!-- <div class="dtTable">
                <div class="dtRow" v-for="item in md" v-show="item.visible" :key="item.id" @click="$parent.centerMyPopup(item)">
                    <div class="dtCell">{{ item.id }}</div>
                    <div class="dtCell">{{ item.region }}</div>
                    <div class="dtCell">{{ [item.parish, item.location].filter(Boolean).join(', ') }}</div>
                    <div class="dtCell">{{ item.title }}</div>
                    <div class="dtCell">{{ item.description }}</div>
                    <div class="dtCell">{{ item.date }}</div>
                    <div class="dtCell" style="width: 180px">{{ item.type }}</div>
                    <div class="dtCell">{{ item.position.lat }},<br/>{{ item.position.lng }}</div>
                    <div class="dtCell" style="text-align: center"><input v-model="item.draggable" type="checkbox" /></div>
                </div>
            </div> -->

        </div>
</template>

<script>
export default {
    name: "VList",
    components: {},
    props: { md: Array },
    data() {
        return {};
    },
    methods: {},
};
</script>

<style scoped>

/* .dtTable{
	display: table;
	width: 100%;
}
.dtRow {
	display: table-row;
}
.dtCell, .dtTableHead {
	border: 1px solid #999999;
	display: table-cell;
	padding: 3px 10px;
}

.dtBody {
	display: table-row-group;
} */


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

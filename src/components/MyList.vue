  <template>

  <div id="xlist">
        <ul id="example-1">
            <li v-for="item in md" :key="item.id">
              {{ item.id }}, {{ item.name }}, {{ item.coordinates }}
            </li>
        </ul>
  </div>
</template>

<script>

import MyData from '../assets/data.json';

export default {
  name: 'MyExample',
  components: {
  },
  props: {md: Array},
  data() {
    return {
      // md: MyData.data,
    };
  },
  methods: {

  },
};
</script>

<style scoped>
#xlist {
  height: 50%;
  overflow: scroll;
}
</style>
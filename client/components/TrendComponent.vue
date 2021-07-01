<template>
  <trend
    :data="PAPP"
    :gradient="['#6fa8dc', '#42b983', '#2c3e50']"
    auto-draw
    smooth
  >
  </trend>
</template>

<script>
import Vue from 'vue'
import Trend from 'vuetrend'
Vue.use(Trend)

import axios from 'axios'

export default {
  data() {
    return { PAPP: [] }
  },
  created() {
    axios
      .get('http://127.0.0.1:5000/consumption')
      .then((response) =>
        Object.keys(response.data.result).forEach((key) => {
          this.PAPP.push(response.data.result[key]['PAPP'])
        })
      )
      .then()
  },
}
</script>

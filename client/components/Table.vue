 <template>
  <v-simple-table>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">ADCO</th>
          <th class="text-left">OPTARIF</th>
          <th class="text-left">ISOUSC</th>
          <th class="text-left">BASE</th>
          <th class="text-left">PTEC</th>
          <th class="text-left">INST</th>
          <th class="text-left">MAX</th>
          <th class="text-left">PAPP</th>
          <th class="text-left">HHPHC</th>
          <th class="text-left">MOTDETAT</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in datas"
          :key="item.PAPP"
          :class="{ overconsumption: item.PAPP > highCeiling }"
        >
          <td>{{ item.ADCO }}</td>
          <td>{{ item.OPTARIF }}</td>
          <td>{{ item.ISOUSC }}</td>
          <td>{{ item.BASE }}</td>
          <td>{{ item.PTEC }}</td>
          <td>{{ item.INST }}</td>
          <td>{{ item.MAX }}</td>
          <td>{{ item.PAPP }}</td>
          <td>{{ item.HHPHC }}</td>
          <td>{{ item.MOTDETAT }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return { datas: {}, highCeiling: 390 }
  },
  created() {
    axios
      .get('http://127.0.0.1:5000/consumption')
      .then((response) => (this.datas = response.data.result))
  },
}
</script>

<style>
.overconsumption {
  background-color: red;
}
</style>
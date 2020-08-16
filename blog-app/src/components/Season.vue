<template>
  <div class="p-3">
    <h3 class="m-2">{{ season.year }}</h3>
    <div>Record: {{ season.wins }} wins - {{ season.losses }} losses</div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      season: {
        year: "",
        wins: "",
        losses: "",
        era_plus: "",
        bat_ave: "",
        ops: "",
        run_diff: "",
      },
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/api/season/" + this.$route.params.id)
      .then((response) => {
        this.season = response.data;
      });
  },
};
</script>
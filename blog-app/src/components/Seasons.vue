<template>
  <div class="p-3">
    <div class="card" v-for="season of seasons" v-bind:key="season.year">
      <div class="col-md-4">
        <h3 class="mt-3">{{ season.year }}</h3>
      </div>
      <div class="card-body">
        <p class="card-text">{{ season.wins }} - {{ season.losses }}</p>
        <router-link
          :to="{name: 'season', params: { id:season.year }}"
          class="btn btn-sm btn-primary"
        >More details</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      seasons: [],
    };
  },
  created() {
    this.all();
  },
  methods: {
    all: function () {
      axios.get("http://127.0.0.1:8000/api/seasons/").then((response) => {
        this.seasons = response.data;
      });
    },
  },
};
</script>
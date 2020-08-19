<template>
  <b-card-body>
    <b-card-title>{{post.title}}</b-card-title>
    <b-card-text>{{post.content}}</b-card-text>
    <b-button :href="url" variant="primary">Link</b-button>
  </b-card-body>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      post: {
        title: "",
        content: "",
        url: "",
      },
      submitted: false,
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/api/posts/" + this.$route.params.id)
      .then((response) => {
        this.post = response.data;
      });
  },
};
</script>
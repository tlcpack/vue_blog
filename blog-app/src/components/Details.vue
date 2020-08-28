<template>
  <div class="jumbotron">
    <div class="display-4">{{post.title}}</div>
    <p class="lead">{{post.content}}</p>
    <a class="btn btn-primary btn-lg" :href="`${post.url}`" target="_blank" role="button">Learn more</a>
    <router-link :to="`/details/${post.id}/comment`" class="m-3 btn btn-sm btn-primary">Comment</router-link>
  </div>
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
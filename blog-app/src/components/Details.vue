<template>
  <div class="pt-5">
    <div>
      <label for="title">Title</label>
      <div>{{ post.title }}</div>
    </div>
    <div>
      <label for="content">Your thoughts:</label>
      <div>{{ post.content }}</div>
    </div>
    <div>
      <label for="url">Associated link?</label>
      <div>{{ post.url }}</div>
    </div>
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
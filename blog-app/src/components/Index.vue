<template>
  <div class="pt-5">
    <div v-if="posts && posts.length">
      <div class="card mb-3" v-for="post of posts" v-bind:key="post.id">
        <div class="row no-gutters">
          <div class="col-md-4">
            <svg
              class="bd-placeholder-img"
              width="200"
              xmlns="http://www.w3.org/2000/svg"
              preserveAspectRatio="xMidYMid slice"
              focusable="false"
              role="img"
              aria-label="Placeholder: Thumbnail"
            >
              <title>{{ post.title }}</title>
              <rect width="100%" height="100%" fill="#55595c" />
              <text x="50%" y="50%" fill="#eceeef" dy=".3em">{{ post.title.charAt(0) }}</text>
            </svg>
          </div>
          <div class="col-md-8">
            <div class="card-body">
              <h5 class="card-title">{{ post.title }}</h5>
              <p class="card-text">{{ post.content }}</p>
              <router-link
                :to="{name: 'edit', params: { id: post.id }}"
                class="btn btn-sm btn-primary"
              >Edit</router-link>
              <button class="btn btn-danger btn-sm ml-1" v-on:click="deletePost(post)">Delete</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <p v-if="posts.length == 0">No Posts</p>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      posts: [],
    };
  },
  created() {
    this.all();
  },
  methods: {
    deletePost: function (post) {
      if (confirm("Delete " + post.title)) {
        axios
          .delete(`http://127.0.0.1:8000/api/posts/${post.id}`)
          .then((response) => {
            this.all();
          });
      }
    },
    all: function () {
      axios.get("http://127.0.0.1:8000/api/posts/").then((response) => {
        this.posts = response.data;
      });
    },
  },
};
</script>
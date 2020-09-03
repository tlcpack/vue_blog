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
              <text x="50%" y="50%" fill="#eceeef" dy=".3em">{{ post.id }}</text>
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
              <router-link
                :to="{name: 'details', params: { id: post.id }}"
                class="btn btn-sm btn-info ml-1"
              >Details</router-link>
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
      axios
        .delete(`http://nameless-spire-79883.herokuapp.com/api/posts/${post.id}`)
        .then((response) => {
          console.log(response);
          this.all();
        });
    },
    all: function () {
      axios.get("http://nameless-spire-79883.herokuapp.com/api/posts/").then((response) => {
        this.posts = response.data;
      });
    },
  },
};
</script>
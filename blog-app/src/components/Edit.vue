<template>
    <div class="pt-5">
    <form @submit.prevent="update" method="post">
      <div class="form-group">
        <label for="title">Title</label>
        <input
          type="text"
          class="form-control"
          id="title"
          v-model="post.title"
          name="title"
          placeholder="Blog Title"
        />
      </div>
      <div class="form-group">
        <label for="content">Your thoughts:</label>
        <input
          type="text"
          class="form-control"
          id="content"
          v-model="post.content"
          name="content"
          placeholder="Write something interesting!"
        />
      </div>
      <div class="form-group">
        <label for="url">Associated link?</label>
        <input
          type="url"
          class="form-control"
          id="url"
          v-model="post.url"
          name="url"
          placeholder="Enter website here"
        />
      </div>
      <button type="submit" class="btn btn-primary">Post!</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
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
        axios.get("http://nameless-spire-79883.herokuapp.com/api/posts/" + this.$route.params.id).then((response) => {
            this.post = response.data;
        });
    },
    methods: {
        update: function () {
            axios.put(`http://nameless-spire-79883.herokuapp.com/api/posts/${this.post.id}/`,
            this.post
            )
            .then((response) => {
                console.log(response);
                this.$router.push("/");
            });
        },
    },
};
</script>
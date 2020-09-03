<template>
  <div class="pt-5">
    <form @submit.prevent="create" method="post">
      <div class="form-group">
        <h3 for="title" class="py-3">{{post.title}}</h3>
        <input
          type="text"
          class="form-control"
          id="title"
          v-model="post.title"
          name="title"
          placeholder="Blog Title"
        />
      </div>
      <div class="form-group my-5">
        <label for="content">Your thoughts:</label>
        <input
          type="text"
          class="form-control"
          id="content"
          v-model="post.content"
          @keyup="charCount()"
          name="content"
          placeholder="Write something interesting!"
        />
      </div>
      <div class="m-3">{{ totalcharacter }} characters used</div>
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
      <b-button type="submit" class="btn btn-primary" v-b-tooltip.hover.bottom title="This is final">Post!</b-button>
    </form>
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
    methods: {
        create: function () {
            this.submitted = true;
            axios.post("nameless-spire-79883.herokuapp.com/api/posts/", this.post)
            .then((response) => {
                console.log(response);
                this.$router.push("/");
            });
        },
        charCount: function () {
          this.totalcharacter = this.post.content.length + 1;
        }
    },
};
</script>
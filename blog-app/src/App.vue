<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <h2 class="d-flex justify-content-center">
          <router-link to="/index">Blog Time!</router-link>
        </h2>
        <div class="row justify-content-center">
        <router-link to='/create' class="m-3 btn btn-sm btn-primary">Create post</router-link>
        <router-link to='/seasons' class="m-3 btn btn-sm btn-secondary">List of seasons</router-link>
        <router-view />
        </div>
      </div>  
    </div>
  </div>
</template>
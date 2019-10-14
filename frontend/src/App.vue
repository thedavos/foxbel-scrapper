<template>
  <div id="app">
    <input v-model="web" type="text" placeholder="Coloque un url. Ej: https://platzi.com">
    <button @click="submitSearchPage">Buscar</button>
    <div class="image">
      <figure v-for="(image, idx) in images" :key="idx">
        <img :src="image" alt="">
      </figure>
    </div>
  </div>
</template>

<script>
export default {
  name: 'app',

  data() {
    return {
      web: "",
      images: []
    }
  },

  methods: {
    submitSearchPage() {
      const basePath = "http://127.0.0.1:5000/api/images?host="
      const host = this.checkLink(this.web)

      fetch(`${basePath}${host}`)
        .then(res => res.json())
        .then(({ results }) => {
          this.images = results
        })
    },

    checkLink(link) {
      if ((!link.includes("https://") || !link.includes("http://")) && link) {
        return `https://${link}`
      } else {
        return link
      }
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

<template>
  <div >
    <form id="search-form">
        <input class="form-text" type="text" id="isbn" placeholder="ISBNコードを入力" v-model="isbn">
        <button type="button" v-on:click="search()">検索</button>
    </form>
    <div id="result">{{ title }}</div>
  </div>
</template>
<script>
import { axios } from "@/common/api.service.js";

export default {
  data() {
    return {
      isbn: '',
      title: '',
    };
  },
  methods: {
    search() {
      // const code = document.getElementById('isbn').value;
      axios.get("https://www.googleapis.com/books/v1/volumes?q=isbn:9784103060765")
        .then((response) => {
          return response.json();
                }).then(data => {
                  const bookTitle = data.items[0].volumeInfo.title;
                  this.title=bookTitle;
                }).catch((error) => {
                    this.title=error;
                });
    },
  },
};
</script>
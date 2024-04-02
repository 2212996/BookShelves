<template>
      <form id="search-form">
        <input class="form-text" type="text" id="isbn" placeholder="ISBNコードを入力" v-model="isbn">
        <button type="button" v-on:click="getResult()">検索</button>
    </form>
    <div id="result">{{ items }}</div>
</template>
<script>
import { axios } from "@/common/api.service.js";

export default {
  data() {
    return {
      query:'',
      items:''
      };
    },
  methods:{
    getResult(){
      axios.get("https://www.googleapis.com/books/v1/volumes?q=isbn:9784103060765").then(response => {
        console.log(response.data);
        this.items = response.data.items[0].volumeInfo.title;
        });
      }
    }
  // data() {
  //   return{
  //     query:'',
  //     items:'',
  //     },
  //   },
  // methods:{
  //   getResult(){
  //     axios.get("https://www.googleapis.com/books/v1/volumes?q=isbn:9784103060765").then(response => {
  //       console.log(response.data);
  //       this.items = response.data.items[0].volumeInfo.title;
  //       });
  //     }
  //   }
};
</script>
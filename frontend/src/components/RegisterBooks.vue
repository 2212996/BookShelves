<template>
  <div class="area">
    <div class="contents">
      <div class="register-title">書籍登録</div>
      <div class="form-area">
        <form id="form1" @submit.prevent="search">
          <label class="selectbox-6">
              <select v-model="searchType">
                  <option value="isbn">ISBN</option>
                  <option value="any">キーワード</option>
              </select>
          </label>
          <div v-if="searchType==='isbn'" class="sbox">
            <input id="sbox1" v-model="keyword" name="s" type="text" placeholder="ISBNコードを入力してください" />
          </div>
          <div v-if="searchType==='any' " class="sbox">
            <input id="sbox1" v-model="keyword" name="s" type="text" placeholder="キーワードを入力してください" />
          </div>
          <input id="sbtn1" type="submit" value="Search" />
        </form>
      </div>
      <div class="result-area">
        <div class="result-title">検索結果</div>
      </div>
      <div class="content">
          <div class="loading" v-if="loadState == 'loading'"></div>
          <v-container fluid grid-list-sm>
            <v-layout row wrap>
              <v-flex v-for="i in 2" :key="i" xs4>
                <BookList v-if="loadState == 'success'" :books="books" :keyword="keyword" :searchType="searchType"/>
              </v-flex>
            </v-layout>
          </v-container>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import BookList from './BookList'

export default {
  data() {
    return {
      books: [],
      keyword: '',
      orderBy: 'newest',
      maxResults: '10',
      loadState: '',
      checked: false,
      tab: 0,
      isbnCodeRules:[value => value.length <= 10 || '10文字以内で入力してください'],
      isbnCode: '',
      searchType: "isbn",
    }
  },
  methods: {
    search() {
      this.loadState = 'loading'
      if(this.searchType=='isbn'){
        axios
        .get(
          `https://www.googleapis.com/books/v1/volumes?q=isbn:${
            this.keyword
          }&orderBy=${this.orderBy}&maxResults=${this.maxResults}`
        )
        .then(response => {
          console.log(response.data.items)
          this.books = response.data.items
          this.loadState = 'success'
        });
      } else{
        axios
        .get(
          `https://www.googleapis.com/books/v1/volumes?q=${
            this.keyword
          }&orderBy=${this.orderBy}&maxResults=${this.maxResults}`
        )
        .then(response => {
          console.log(response.data.items)
          this.books = response.data.items
          this.loadState = 'success'
        });
      }
    }
  },
  components: {
    BookList
  }
}
</script>
<style>
.area{
  width: 100%;
  background-color: #F4F5F7;
  padding-bottom: 10vh;
}
.contents{
  width: 85%;
  margin:auto;
}
.register-title{
  text-align: left;
  font-weight: bold;
  padding-top:30px;
  padding-bottom:30px;
  color:#4F5272;
  font-size: 20px;
}
.form-area{
  width:100%;
}
#form1{
  display: flex;
  justify-content: left;
  height:40px;
}
.selectbox-6 {
    position: relative;
}
/* 選択ボタンのマーク */
.selectbox-6::before,
.selectbox-6::after {
    position: absolute;
    right: 15px;
    width: 9px;
    height: 6px;
    background-color: #535353;
    content: '';
    pointer-events: none;
}
.selectbox-6::before {
    top: calc(50% - 9px);
    clip-path: polygon(50% 0, 100% 100%, 0 100%);
}
.selectbox-6::after {
    bottom: calc(50% - 9px);
    clip-path: polygon(0 0, 50% 100%, 100% 0);
}
/* 選択ボタンのマークおわり */
.selectbox-6 select {
    appearance: none;
    width: 140px;
    height: 40px;
    padding: .4em calc(.8em + 30px) .4em .8em;
    border: 1px solid #d0d0d0;
    border-radius: 3px;
    background-color: #fff;
    color: #666;
    font-size:16px;
    cursor: pointer;
}
.sbox{
  width:25%;
}
#sbox1{
  width:100%;
  padding:0 15px;
  border-radius:4px 0 0 4px;
  background:#eee;
  border:none;
  outline:0;
  height:40px;
}
#sbtn1{
  width:70px;
  border-radius:0 4px 4px 0;
  background:#81B29A;
  border:none;
  color:#fff;
  font-size:16px;
  cursor: pointer;
  height:40px;
}
#sbtn1:hover {
  background: #92dbff;
}
.isbn-code-form{
  width:50%;
}
.isbn-code-form-button{
  width:20%;
  margin-left: auto;
}
.result-title{
  text-align: left;
  font-weight: bold;
  padding-top:30px;
  padding-bottom:30px;
  color:#4F5272;
  font-size: 20px;
}
</style>
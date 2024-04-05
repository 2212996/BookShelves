<template>
  <div class="area">
    <div class="contents">
      <div class="register-title">書籍登録</div>
      <div class="form-area">
        <form id="form1" @submit.prevent="search">
          <input id="sbox1" v-model="keyword" name="s" type="text" placeholder="ISBNコードを入力してください" />
          <input id="sbtn1" type="submit" value="Search" />
        </form>
          <!-- <v-form fast-fail @submit.prevent class="isbn-code-box">
            <v-text-field
            class="isbn-code-form"
            v-model="isbnCode"
            :rules="isbnCodeRules"
            label="ISBNコードを入力してください"
          ></v-text-field>
          </v-form>
          <v-btn class="isbn-code-form-button" type="submit">Submit</v-btn> -->
        <!-- <v-form fast-fail @submit.prevent class="isbn-code-box">
          <v-text-field
            class="isbn-code-form"
            v-model="isbnCode"
            :rules="isbnCodeRules"
            label="ISBNコードを入力してください"
          ></v-text-field>
          <v-btn class="isbn-code-form-button" type="submit" inline>Submit</v-btn>
        </v-form> -->
      </div>
        <!-- <div class="query">
        <form @submit.prevent="search">
            <div class="isbn-form">
            <input type="text" v-model="keyword" placeholder="Search..." class="form-control isbn-form-box" required>
            <input type="submit" value="Search" class="btn btn-primary isbn-form-btn">
            </div>
            <div>
            </div>
        </form>
        </div> -->
        <div class="result-area">
          <div class="result-title">検索結果</div>
        </div>
        <div class="content">
            <div class="loading" v-if="loadState == 'loading'"></div>
            <BookList v-if="loadState == 'success'" :books="books" :keyword="keyword"/>
        </div>
        <!-- <div class="btn btn-primary">
            <input type="checkbox" id="checkbox" v-model="checked" />
            <label for="checkbox">{{ checked }}</label>
        </div>
        <div v-if="checked">
            <ShowDataBase />
        </div> -->
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
      isbnCode: ''
    }
  },
  methods: {
    search() {
      this.loadState = 'loading'
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
        })
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
  justify-content: left; /*中央へ固定*/	
  height:40px;/*高さ*/	
}
/*入力フォーム*/
#sbox1{
  width:25%;/*横幅*/
  padding:0 15px;/*プレースホルダーの位置調整*/
  border-radius:4px 0 0 4px;/*左側の角を少し丸める*/		
  background:#eee;/*検背景カラー*/
  border:none;/*枠線を消す*/ 
  outline:0;/*クリック時の青い枠線消す*/	
}
/*検索ボタン*/
#sbtn1{
  width:70px;/*横幅*/ 
  border-radius:0 4px 4px 0;/*右側の角を少し丸める*/
  background:#81B29A;/*背景カラー*/ 
  border:none;/*枠線を消す*/ 
  color:#fff;/*テキストカラー*/ 
  font-size:16px;/*フォントサイズ指定*/ 
  cursor: pointer;/*マウスを乗せると指差しポインターになる*/
}
/*検索ボタンマウスオーバー時*/
#sbtn1:hover {
  background: #92dbff;/*背景カラー変更*/
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
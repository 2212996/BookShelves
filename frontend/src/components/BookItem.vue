<template>
    <div class="book-item">
        <div class="book-item-table">
            <div class="book-item-image">
                <template v-if="volumeInfo.imageLinks">
                    <img :src="volumeInfo.imageLinks.thumbnail" :alt="volumeInfo.title" height="100">
                </template>
                <template v-else>
                    <img
                    src="https://islandpress.org/sites/default/files/400px%20x%20600px-r01BookNotPictured.jpg"
                    :alt="volumeInfo.title"
                    height="100"
                    >
                </template>
            </div>
            <div class="title">
                <div class="inner">
                    {{ volumeInfo.title }}
                </div>
            </div>
            <div class="author">
                <div class="inner">
                    <span v-if="!volumeInfo.authors">No authors to display</span>
                    <span v-else>
                    By
                        <span v-for="(author, authorindex) in volumeInfo.authors" :key="authorindex">
                            <em>
                            {{
                            index + 1 !== volumeInfo.authors.length && authorindex + 1 !== book.volumeInfo.authors.length-1 ? author + ', ' : authorindex + 1 == book.volumeInfo.authors.length && authorindex+1 !== 1 ? ' and ' + author : author
                            }}
                            </em>
                        </span>
                    </span>
                </div>
            </div>
            <div class="publisher">
                <div class="inner">{{ volumeInfo.publisher }}</div>
            </div>
            <div class="submit-button">
                <div class="inner">
                    <button v-on:click="submitBookData()" class="button">登録する</button>
                </div>
            </div>
        </div>
        <!-- <a :href="volumeInfo.previewLink" target="_blank"> -->

        <!-- <p>{{ keyword }}</p> -->

        <!-- <h4>{{ volumeInfo.title }}</h4> -->

        <!-- <p class="author">
            <span v-if="!volumeInfo.authors">No authors to display</span>
            <span v-else>
            By
            <span v-for="(author, index) in volumeInfo.authors" :key="index">
                <em>
                {{
                index + 1 !== volumeInfo.authors.length && index + 1 !== book.volumeInfo.authors.length-1 ? author + ', ' : index + 1 == book.volumeInfo.authors.length && index+1 !== 1 ? ' and ' + author : author
                }}
                </em>
            </span>
            </span>
        </p> -->

        <!-- <p class="publisher">{{ volumeInfo.publisher }}</p> -->

        <!-- </a> -->

        <!-- <button v-on:click="submitBookData()" class="button">登録する</button> -->
        <div>{{ testData }}</div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
data(){
    return {
        testData: "",
    }
},
props: {
    book: {
        type: Object,
        required: true
    },
    keyword: {
        type: String
    }
},
computed: {
    volumeInfo(){
    return this.book.volumeInfo;
    }
},
methods: {
    async submitBookData(){
        // this.testData = this.book.volumeInfo.title;
        const formData = new FormData();
        formData.append("ISBN", this.keyword);
        formData.append("Title", this.book.volumeInfo.title);
        formData.append("Author", this.book.volumeInfo.authors[0]);
        formData.append("Publisher", this.book.volumeInfo.published);
        console.log(this.keyword);
        try {
            const endpoint = "/api/v2/bookdata/";
            await axios.post(endpoint, formData, {
            headers: {
                "Content-Type": "multipart/form-data",
            },
            });
            alert("Success!");
        } catch (error) {
            console.log(error);
            alert("No!");
        }
    }
}
}
</script>

<style scoped>
.book-item{
    margin-bottom: 5px;
    background-color: #FFF;
    height:125px;
}
.book-item-table{
    display: flex;
    vertical-align: middle;
    height:125px;
}
.book-item-image{
    width:10%;
    height: 100%;
    padding-top:12.5px;
    padding-bottom:12.5px;
}
.title{
    width:27.5%;
    height: 100%;
    display: table;
}
.inner{
    display: table-cell;
    vertical-align: middle;
}
.author{
    width:25%;
    height: 100%;
    display: table;
}
.publisher{
    width:25%;
    height: 100%;
    display: table;
}
.submit-button{
    width:10%;
    height: 100%;
    display: table;
}
/* ul {
padding: 0;
}

ul li {
display: inline-block;
}

ul li:first-child {
list-style: none;
}
.author {
font-size: 14px;
}

.button {
  border: 0;
  padding: 0 10px;
  margin: 0;
  background: #B22D35;
  color: white;
  box-shadow: 0 0 0 transparent;

  height: 30px;
  vertical-align: top;
} */
</style>

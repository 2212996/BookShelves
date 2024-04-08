<template>
    <div class="book-item">
        <v-container>
            <v-row no-gutters>
                <v-col cols="4">
                    <div class="book-item-image">
                        <template v-if="volumeInfo.imageLinks">
                            <img :src="volumeInfo.imageLinks.thumbnail" :alt="volumeInfo.title" class="pic">
                        </template>
                        <template v-else>
                            <img
                            src="https://islandpress.org/sites/default/files/400px%20x%20600px-r01BookNotPictured.jpg"
                            :alt="volumeInfo.title"
                            >
                        </template>
                    </div>
                </v-col>
                <v-col cols="8" class="info">
                    <!-- <v-row>
                        <v-col cols="12"></v-col>
                    </v-row> -->
                    <div class="title">
                        {{ volumeInfo.title }}
                    </div>
                    
                    <div class="author">
                        <div v-if="!volumeInfo.authors">No authors to display</div>
                        <div v-else>著者：{{ volumeInfo.authors[0] }}</div>
                    </div>
                    <div class="publisher">
                        出版社：{{ volumeInfo.publisher }}
                    </div>
                    <div class="isbn">
                        <div v-for="(code, count) in volumeInfo.industryIdentifiers" :key="count">
                            <div v-if="code.type='ISBN_13'">
                                ISBN:{{ code.identifier }}
                            </div>
                        </div>
                    </div>
                    <div class="void"></div>
                    <div class="submit-button">
                        <v-btn v-on:click="submitBookData()" variant="tonal" color="#E07A5F">登録する</v-btn>
                    </div>
                </v-col>
            </v-row>
        </v-container>
        <!-- <div class="book-item-table">
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
        </div> -->
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
    margin-bottom: 10px;
    margin-left: 10px;
    background-color: #FFF;
    /* height:200px; */
    text-align:left;
    width:40vw;
    border-radius: 10px;
}
/* .book-item-table{
    display: flex;
    vertical-align: middle;
    height:125px;
} */
.book-item-image{
    /* width:10%; */
    height: 100%;
    /* padding-top:5px;
    padding-bottom:10px; */
    width:100%;
    /* background-color: aqua; */
}
.pic{
    height:100%;
}
.info{
    /* background-color: aqua; */
    position: relative;
}
.title{
    height:25%;
    font-size: 18px;
    font-weight: bold;
}
.author{
    height:15%;
}
.publisher{
    height:15%;
}
.isbn{
    height:15%;
}
.void{
}
.submit-button{
    position: absolute;
	bottom: 0;
}
</style>

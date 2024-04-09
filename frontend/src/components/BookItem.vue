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
		},
		searchType: {
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
			const formData = new FormData();
			if(this.searchType=="isbn"){
				formData.append("ISBN", this.keyword);
			} else{
				formData.append("ISBN", 0);
			}
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
	text-align:left;
	width:40vw;
	border-radius: 10px;
}
.book-item-image{
	height: 100%;
	width:100%;
}
.pic{
	height:100%;
}
.info{
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
.submit-button{
	position: absolute;
	bottom: 0;
}
</style>

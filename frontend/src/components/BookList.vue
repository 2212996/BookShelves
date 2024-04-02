<template>
<div class="book-list">
    <BookItem v-for="book in books" :key="book.id" :book="book" :keyword="keyword"/>
</div>
</template>

<script>
import BookItem from "./BookItem";

export default {
props: {
    books: {
        type: Array,
        required: true
    },
    keyword: {
        type: String
    }
},
components: {
    BookItem
}
};
</script>

<style>
</style>
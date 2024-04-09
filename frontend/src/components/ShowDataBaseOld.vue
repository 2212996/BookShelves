<template>
<div>
    <table>
        <tr>
            <th>ID</th>
            <th>ISBN</th>
            <th>Title</th>
            <th>Author</th>
            <th>Publisher</th>
            <th>Action</th>
        </tr>
        <tr  v-for="(data, index) in response.data" :key="index">
            <td>{{ data.id }}</td>
            <td>{{ data.isbn }}</td>
            <td>{{ data.title }}</td>
            <td>{{ data.author }}</td>
            <td>{{ data.publisher }}</td>
            <td>
                <button
                class="btn btn-info">
                編集
                </button>
                <button
                class="btn btn-danger"
                v-on:click="deleteDataa(data.id)">
                削除
                </button>
            </td>
        </tr>
    </table>
    <!-- <div  v-for="(data, index) in response.data" :key="index">
        {{ data }}
    </div> -->
</div>
</template>

<script>
import axios from 'axios'

export default {
    data(){
        return {
            response: ""
        }
    },
mounted: function() {
 this.getArticles();
},
    name: 'ShowDataBase',
    methods:{
        getArticles: async function()  {
            const endpoint = "/api/v2/bookdata/";
            this.response = await axios.get(endpoint);
        },
        async deleteDataa(id){
            const endpoint = "/api/v2/bookdata/"+id;
            await axios.delete(endpoint)
            .then(() => {
                this.getArticles();
            })
            .catch((err) => {
            console.log(err);
            });
        }
    }
    }
</script>
<template>
    <div class="area">
        <div class="contents">
            <div class="database-title">データベース</div>
            <div class="database-table">
                <v-container>
                    <v-row>
                        <v-col cols="12">
                            <v-data-table
                            :headers="headers"
                            :items="serverDatas"
                            class="table_to_custom"
                            >
                                <template v-slot:[`item.isbn`]="{ item }">
                                    <div align="left">{{ item.isbn }}</div>
                                </template>
                                <template v-slot:[`item.title`]="{ item }">
                                    <div align="left">{{ item.title }}</div>
                                </template>
                                <template v-slot:[`item.author`]="{ item }">
                                    <div align="left">{{ item.author }}</div>
                                </template>
                                <template v-slot:[`item.publisher`]="{ item }">
                                    <div align="left">{{ item.publisher }}</div>
                                </template>
                                <template v-slot:[`item.delete`]="{ item }">
                                    <v-btn
                                        small
                                        color="#81B29A"
                                        @click="deleteItem(item.id)"
                                        class="edit"
                                    >
                                        編集する
                                    </v-btn>
                                    <v-btn
                                        small
                                        color="#E07A5F"
                                        @click="deleteItem(item.id)"
                                    >
                                        削除する
                                    </v-btn>
                                </template>
                            <!-- <template v-slot:item="{item}">
                                <td class="text-xs-center">{{ item.id }}</td>
                                <td class="text-xs-center">{{ item.isbn }}</td>
                                <td class="text-xs-center">{{ item.title }}</td>
                                <td class="text-xs-center">{{ item.author }}</td>
                                <td class="text-xs-center">{{ item.publisher }}</td>
                                <v-btn
                                    small
                                    color="error"
                                    @click="deleteItem(item.id)"
                                >
                                    delete
                                </v-btn>
                            </template> -->
                            </v-data-table>
                        </v-col>
                    </v-row>
                </v-container>
            </div>
        </div>
        <!-- {{ this.serverDatas[0] }} -->
        <!-- {{ this.test }}
        {{ this.testtt }}
        {{ this.items[0] }} -->
    </div>
</template>
<script>
import axios from 'axios'

export default {
  data(){
    return {
      headers: [
          { 
            title: 'ID', value: 'id', width: '5%', align: 'center'
          },
          {
            title: 'ISBN', value: 'isbn', width: '15%', align: 'start'
          },
          { 
            title: 'Title', value: 'title', width: '20%', align: 'start'
          },
          { 
            title: 'Author', value: 'author', width: '20%', align: 'start'
          },
          { 
            title: 'Publisher', value: 'publisher', width: '20%', align: 'start'
          },
          { 
            title: 'Action', value: 'delete', sotrable:false, width: '20%', align: 'start'
          },
        ],
        serverDatas:[],
        test:"",
        items:[],
        testtt:"",
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
            this.serverDatas = this.response.data;
        },
        async deleteItem(id){
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
.database-title{
  text-align: left;
  font-weight: bold;
  padding-top:30px;
  padding-bottom:30px;
  color:#4F5272;
  font-size: 20px;
}
.database-table{
    width:100%;
    /* text-align: left; */
    /* background-color: aqua; */
}
.table_to_custom th{
    background-color: #656994;
    color:#fff;
    font-weight: bold !important;;
}
.edit{
    margin-right: 10px;
}
</style>
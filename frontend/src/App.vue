<template>
  <div id="app" class="app center-block">
    <div class="head-bar"></div>
    <div class="page-bar">
      <v-tabs color="#4F5272" v-model="tab" class="page-bar-tabs">
        <v-tab value="1">register</v-tab>
        <v-tab value="2">database</v-tab>
      </v-tabs>
      <v-window v-model="tab">
        <v-window-item value="1">
          <RegisterBooks />
        </v-window-item>
        <v-window-item value="2">
          <ShowDatabase />
        </v-window-item>
      </v-window>
    </div>
    </div>
</template>

<script>
import RegisterBooks from '@/components/RegisterBooks'
import ShowDatabase from '@/components/ShowDatabase'

export default {
  data() {
    return {
      tab: 0
    }
  },
  components: {
    RegisterBooks,
    ShowDatabase
  }
}
</script>
<style>
.app{
  width: 100%;
  height: 100vh;
  margin: auto;
  text-align: center;
  background-color: #F4F5F7;
  font-family:"Yu Gothic", "游ゴシック", YuGothic, "游ゴシック体";
}
.head-bar{
  width:100%;
  height:10vh;
  background-color: #656994;
}
.page-bar{
  width:100%;
  color:#777;
  background-color: #ffffff;
}
.page-bar-tabs{
  padding-left: 3vw;
}
</style>

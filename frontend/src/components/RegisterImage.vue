<template>
    <div>
      <form @submit.prevent="onSubmit">
        <div>画像</div>
        <div>
          <input
            type="file"
            name=""
            id="img-upload"
            ref="file"
            multiple="multiple"
            @change="uploadFile"
            @click="
              (e) => {
                e.target.value = '';
              }
            "
          />
        </div>
        <button>登録</button>
      </form>
      <!-- プレビュー表示． -->
      <img :src="imgUrl" />
    </div>
  </template>
  
  <script>
  import { axios } from "@/common/api.service.js";
  
  export default {
    data() {
      return {
        imgData: null,
        imgUrl: null,
      };
    },
    methods: {
      uploadFile() {
        this.imgData = this.$refs.file.files[0];
        if (!this.imgData) {
          return;
        }
      },
      async onSubmit() {
        const formData = new FormData();
        formData.append("imageData", this.imgData);
        console.log(this.imgData);
        try {
          const endpoint = "/api/v1/image/";
          const response = await axios.post(endpoint, formData, {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          });
          this.imgUrl = `http://localhost:8000${response.data}`;
          alert("Success!");
        } catch (error) {
          console.log(error);
          alert(error.response.data);
        }
        this.imgData = null;
      },
    },
  };
  </script>
  
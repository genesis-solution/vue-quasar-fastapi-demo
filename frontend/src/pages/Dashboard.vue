<template>
    <q-page>
      <q-card class="q-pa-md">
        <q-card-section class="text-center">
          <h2 class="text-h4">Welcome! {{ name }}</h2>
          <div>
            <alert :message="alertMessage"></alert>
          </div>
          <q-form @submit.prevent="changepassword" class="form-signin">
            <q-input
              outlined
              v-model="password"
              label="Current password"
              type="password"
              class="input-signin"
              required
            />
            <q-input
              outlined
              v-model="new_password"
              label="New Password"
              type="password"
              class="input-signin"
              required
            />
            <q-btn type="submit" color="primary" label="Change password" class="button-signin" />
          </q-form>
        </q-card-section>
      </q-card>
    </q-page>
  </template>

<style>
.form-signin {
    margin: auto;
    text-align: center;
}
.input-signin {
  width: 250px;
  margin: auto;
  margin-bottom: 20px;
}
.button-signin {
    width: 250px;
    margin-bottom: 10px;
}
.link-signin {
    text-align: center;
    margin: auto;
}
.text-center {
    text-align: center;
}
.margin-top-20 {
    margin-top: 20px;
}
</style>
  
  <script>
  import axios from 'axios';
  import Alert from '../components/Alert.vue'

  export default {
    components: {
      Alert
    },
    data() {
      return {
        name: localStorage.getItem("name"),
        password: '',
        new_password:'',
        alertMessage: 'Change password!'
      };
    },
    methods: {
    changepassword() {
        // handle sign in logic here
        axios.post('http://localhost:8000/changepassword', {
            user_id: localStorage.getItem("userid"),
            new_password: this.new_password,
            password: this.password
        })
        .then((response) => {
            if (response.data.status == 200) {
                this.alertMessage = "Successfully changed"
            }
            else {
                this.alertMessage = "Your current password is incorrect."
            }
        })
        .catch((error) => {
            console.log(error);
        });
      },
    },
  };
  </script>
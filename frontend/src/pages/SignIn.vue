<template>
    <q-page>
      <q-card class="q-pa-md">
        <q-card-section class="text-center">
          <h2 class="text-h4">Sign In</h2>
          <div>
            <alert :message="alertMessage"></alert>
          </div>
          <q-form @submit.prevent="signIn" class="form-signin">
            <q-input
              outlined
              v-model="email"
              label="Email"
              type="email"
              class="input-signin"
              required
            />
            <q-input
              outlined
              v-model="password"
              label="Password"
              type="password"
              class="input-signin"
              required
            />
            <q-btn type="submit" color="primary" label="Sign In" class="button-signin" />
          </q-form>
          <router-link to="/register" class="link-signin margin-top-20">To Register</router-link>
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
        email: 'jon@testmail.com',
        password: 'password',
        alertMessage: ''
      };
    },
    methods: {
      signIn() {
        // handle sign in logic here
        axios.post('http://localhost:8000/signin', {
            email: this.email,
            password: this.password
        })
        .then((response) => {
            if (response.data.status == 200) {
              this.alertMessage = ""
              localStorage.setItem("userid", response.data.data[0]);
              localStorage.setItem("name", response.data.data[1] + " " + response.data.data[2])
              this.$router.push('/dashboard')
            }
            else {
              this.alertMessage = "Authentication error!"
            }
        })
        .catch((error) => {
            console.log(error);
        });
      },
    },
  };
  </script>
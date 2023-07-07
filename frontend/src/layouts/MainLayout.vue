<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>
          Demo App
        </q-toolbar-title>

        <div>
          <q-btn type="submit" color="default" class="q-btn--small q-btn--no-uppercase nav-signin" @click="goToSignin" :label="signin"  />
        </div>
      </q-toolbar>
    </q-header>

    <!-- <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
    >
      <q-list>
        <q-item-label
          header
        >
          Essential Links
        </q-item-label>

        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer> -->

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<style>
  .nav-signin {
    border: none !important;
    border-style: none !important;
    border-bottom: none !important;
    background: none;
    box-shadow: none !important;
  }
  .q-btn:before {
    box-shadow: none !important;
  }
</style>

<script>
import EssentialLink from 'components/EssentialLink.vue'

const linksList = [
  {
    title: 'Docs',
    caption: 'quasar.dev',
    icon: 'school',
    link: 'https://quasar.dev'
  }
];

import { defineComponent, ref } from 'vue'

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink
  },
  data() {
      return {
        signin: localStorage.getItem('userid') != null ? "Sign out" : "Sign in"
      };
    },
  methods: {
    goToSignin() {
      if (localStorage.getItem('userid') != null)
      {
        localStorage.clear()
      }
      this.$router.push('/signin')
    }
  },
  setup () {
    const leftDrawerOpen = ref(false)

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  }
})
</script>

<template>
  <div>
    <!-- <h1>Edit Article</h1> -->
    <article-form :article="article" action="update">

    </article-form>
  </div>

</template>

<script>
import ArticleForm from '@/components/ArticleForm.vue'
import { mapGetters, mapActions } from 'vuex'
  export default {
    name: 'AritcleEditView',
    components: { ArticleForm },
    computed: {
      ...mapGetters(['article', 'isArticle',])
    },
    methods: {
      ...mapActions(['fetchArticle', 'update'])
    },
    created() {
      this.fetchArticle(this.$route.params.articlePk)
    },
  }
</script>

<style></style>

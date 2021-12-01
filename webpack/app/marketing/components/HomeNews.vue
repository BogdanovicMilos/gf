<template>
  <div v-if="posts.length" class="home_news">
    <div class="container">
      <div class="home_news__header">
        <h2 class="section_title" data-aos="fade-up" data-aos-delay="100">
          News feed:
        </h2>
        <a href="/blog" class="home_news__more_link aos-init aos-animate" data-aos="fade" data-aos-delay="200">READ WHOLE BLOG ARTICLES</a>
      </div>
      <div class="home_news__slider_wrap">
        <div class="home_news__slider">
          <div class="home_news__slider-list">
            <a v-for="(post, idx) in posts" :key="idx" :href="post.link" class="home_news__itm">
              <div class="home_news__itm-img">
                <img v-if="post._embedded && post._embedded['wp:featuredmedia']" :src="post._embedded['wp:featuredmedia'][0].source_url">
                <img v-else :src="'/static/marketing/img/blog-1.jpg'">
              </div>
              <div class="home_news__itm-info">
                <div v-if="post.title" class="home_news__itm-title">{{ post.title.rendered }}</div>
                <!-- eslint-disable-next-line vue/no-v-html -->
                <div v-if="post.content" class="home_news__itm-descr" v-html="$sanitize(post.content.rendered)" />
                <div v-if="post._embedded && post._embedded.author" class="home_news__itm-meta">
                  Posted on {{ dayjs(post.date).format('MMMM D, YYYY') }} by {{ post._embedded.author[0].name }}
                </div>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import dayjs from "dayjs";

export default {
  data() {
    return {
      "posts": []
    };
  },
  created() {
    this.getPosts();
  },
  methods: {
    dayjs,
    async getPosts() {
      try {
        const response = await axios.get(`/blog/wp-json/wp/v2/posts?_embed&per_page=3&order=desc`);
        this.posts = response.data;
      } catch (error) {
        if (error.response) {
          this.validationErrors = error.response.data;
        } else {
          this.response = "Request failed, try again.";
        }
      }
    }
  }
};
</script>

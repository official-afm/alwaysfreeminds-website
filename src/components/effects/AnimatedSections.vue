<template>
  <div class="animated-sections">
    <!-- Intersection Observer targets for animations -->
    <div class="observer-container">
      <div 
        v-for="(section, index) in sections" 
        :key="index"
        :ref="`section-${index}`"
        class="section-observer"
        :class="[
          'transform transition-all duration-1000 ease-out',
          section.isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'
        ]"
      >
        <slot :name="`section-${index}`" :isVisible="section.isVisible" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AnimatedSections',
  props: {
    sectionCount: {
      type: Number,
      default: 6
    }
  },
  data() {
    return {
      sections: [],
      observer: null
    }
  },
  mounted() {
    this.initializeSections();
    this.setupIntersectionObserver();
  },
  beforeUnmount() {
    if (this.observer) {
      this.observer.disconnect();
    }
  },
  methods: {
    initializeSections() {
      this.sections = Array(this.sectionCount).fill().map(() => ({
        isVisible: false
      }));
    },
    
    setupIntersectionObserver() {
      const options = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
      };
      
      this.observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          const index = parseInt(entry.target.getAttribute('data-index'));
          if (entry.isIntersecting) {
            this.sections[index].isVisible = true;
          }
        });
      }, options);
      
      this.$nextTick(() => {
        this.sections.forEach((_, index) => {
          const element = this.$refs[`section-${index}`]?.[0];
          if (element) {
            element.setAttribute('data-index', index);
            this.observer.observe(element);
          }
        });
      });
    }
  }
}
</script>

<style scoped>
.section-observer {
  min-height: 50px;
}
</style>

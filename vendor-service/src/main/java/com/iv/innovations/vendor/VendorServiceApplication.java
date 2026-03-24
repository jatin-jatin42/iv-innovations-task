package com.iv.innovations.vendor;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@SpringBootApplication
public class VendorServiceApplication {

    public static void main(String[] args) {
        SpringApplication.run(VendorServiceApplication.class, args);
    }

    @Bean
    public WebMvcConfigurer corsConfigurer() {
        return new WebMvcConfigurer() {
            @Override
            public void addCorsMappings(CorsRegistry registry) {
                // Allows cross-origin requests from frontend (Nginx port 80 / localhost)
                registry.addMapping("/**").allowedOrigins("*").allowedMethods("*");
            }
        };
    }
}

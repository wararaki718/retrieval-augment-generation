package com.wararaki.sampleragapplication

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.autoconfigure.data.elasticsearch.ElasticsearchDataAutoConfiguration
import org.springframework.boot.runApplication
import org.springframework.data.elasticsearch.repository.config.EnableElasticsearchRepositories

@EnableElasticsearchRepositories
@SpringBootApplication(exclude = [ElasticsearchDataAutoConfiguration::class])
class SampleRagApplication

fun main(args: Array<String>) {
	runApplication<SampleRagApplication>(*args)
}

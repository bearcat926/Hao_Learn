package hao.es;

import net.logstash.logback.appender.LogstashTcpSocketAppender;
import net.logstash.logback.appender.destination.DelegateDestinationConnectionStrategy;
import net.logstash.logback.encoder.LogstashEncoder;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class EsdemoApplication {

	public static void main(String[] args) {
		SpringApplication.run(EsdemoApplication.class, args);
	}

}

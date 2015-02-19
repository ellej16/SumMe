import py4j.GatewayServer;
import com.cybozu.labs.langdetect.Detector;
import com.cybozu.labs.langdetect.DetectorFactory;
import com.cybozu.labs.langdetect.Language;
import com.cybozu.labs.langdetect.*;

public class LangDetect
{
	public void init(String profileDirectory) throws LangDetectException
	{
		DetectorFactory.loadProfile(profileDirectory);
	}

	public String detect(String text)throws LangDetectException
	{
		Detector detector = DetectorFactory.create();
		detector.append(text);
		return detector.detect();
	}

	public static void main(String args[])
	{
		LangDetect app = new LangDetect();
		GatewayServer server = new GatewayServer(app);
		server.start();
	}

}